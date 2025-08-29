"""from openai import OpenAI
import openai
import telebot
from telebot import formatting
# ضع مفتاح OpenAI هنا
openai.api_key = ""
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)
client = OpenAI()

def gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ===== معالجة النص =====
def process_text(bot, message):
    text = message.text
    reply = gpt_response(text)
    bot.send_message(message.chat.id, f"🤖 GPT: {reply}")

# ===== معالجة الملفات =====
def process_file(bot, message):
    if not message.document:
        bot.send_message(message.chat.id, "❌ لم يتم استلام ملف.")
        return
    file_info = bot.get_file(message.document.file_id)
    downloaded = bot.download_file(file_info.file_path)
    filename = message.document.file_name
    with open(filename, "wb") as f:
        f.write(downloaded)

    text_content = ""
    if filename.endswith(".txt"):
        with open(filename, "r", encoding="utf-8") as f:
            text_content = f.read()

    reply = gpt_response(text_content or f"لقد استلمت ملف باسم {filename}")
    bot.send_message(message.chat.id, f"🤖 GPT: {reply}")

# ===== معالجة الصوت =====
def process_audio(bot, message):
    file_id = message.audio.file_id if message.audio else message.voice.file_id
    file_info = bot.get_file(file_id)
    downloaded = bot.download_file(file_info.file_path)
    filename = f"{message.from_user.id}_voice.ogg"
    with open(filename, "wb") as f:
        f.write(downloaded)

    
    audio_file = open(filename, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_text = transcript.text



    reply = gpt_response(audio_text)
    bot.send_message(message.chat.id, f"🤖 GPT: {reply}")

# ===== معالجة الفيديو =====
def process_video(bot, message):
    file_info = bot.get_file(message.video.file_id)
    downloaded = bot.download_file(file_info.file_path)
    filename = f"{message.from_user.id}_video.mp4"
    with open(filename, "wb") as f:
        f.write(downloaded)
    
    bot.send_message(message.chat.id, f"🤖 استلمت الفيديو: {filename} (يمكن تحويله لصوت لاحقاً)")
"""
import os
import openai
from openai import OpenAI

import telebot
from telebot import types

from pypdf import PdfReader
from docx import Document as DocxDocument

from faster_whisper import WhisperModel
from pydub import AudioSegment

from chat.chat_markup import main_chat_menu, markup_chat_data

# ===== مفاتيح =====
openai.api_key = ""
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
client = OpenAI(api_key=openai.api_key)

# ===== تعريف ffmpeg لـ pydub =====
AudioSegment.converter = r"E:\ffmpeg\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

# ===== إعداد نموذج faster-whisper =====
model = WhisperModel("small", device="cpu", compute_type="int8")

# ===== دالة التواصل مع GPT =====
def gpt_response(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ حدث خطأ مع GPT: {e}"

# ===== الرد على النصوص =====
def process_text(bot, message):
    reply = gpt_response(message.text)
    bot.send_message(chat_id=message.chat.id, text=f"🤖 GPT:\n{reply}")


MAX_LENGTH = 4000  # Telegram limit buffer

def send_long_message(bot, chat_id, text):
    for i in range(0, len(text), MAX_LENGTH):
        bot.send_message(chat_id, text[i:i+MAX_LENGTH])

# ===== الرد على الملفات =====
def process_file(bot, message):
    if not message.document:
        bot.send_message(message.chat.id, "❌ لم يتم استلام ملف.")
        return

    file_info = bot.get_file(message.document.file_id)
    downloaded = bot.download_file(file_info.file_path)
    filename = message.document.file_name

    with open(filename, "wb") as f:
        f.write(downloaded)

    text_content = ""
    if filename.endswith(".txt"):
        with open(filename, "r", encoding="utf-8") as f:
            text_content = f.read()
    elif filename.endswith(".pdf"):
        reader = PdfReader(filename)
        text_content = "\n".join(page.extract_text() or "" for page in reader.pages)
    elif filename.endswith(".docx"):
        doc = DocxDocument(filename)
        text_content = "\n".join(p.text for p in doc.paragraphs)

    reply = gpt_response(text_content or f"لقد استلمت ملف باسم {filename}")
    send_long_message(bot, message.chat.id, f"🤖 GPT:\n{reply}")

# ===== الرد على الصوت =====
def process_audio(bot, message):
    file_id = message.audio.file_id if message.audio else message.voice.file_id
    file_info = bot.get_file(file_id)
    downloaded = bot.download_file(file_info.file_path)

    ogg_filename = f"{message.from_user.id}_voice.ogg"
    with open(ogg_filename, "wb") as f:
        f.write(downloaded)

    audio_path = f"{message.from_user.id}_voice.mp3"
    sound = AudioSegment.from_ogg(ogg_filename)
    sound.export(audio_path, format="mp3")

    segments, info = model.transcribe(audio_path, vad_filter=True)
    audio_text = " ".join(seg.text.strip() for seg in segments)

    reply = gpt_response(audio_text)
    bot.send_message(chat_id=message.chat.id, text=f"🤖 GPT:\n{reply}")


from moviepy import VideoFileClip
from pydub import AudioSegment

def process_video(bot, message):
    print("وصلت لـ process_video:", message)
    
    # Check for video
    if message.video:
        file_id = message.video.file_id
        filename = f"{message.from_user.id}_video.mp4"
    # Check for document that is a video
    elif message.document and message.document.mime_type.startswith("video"):
        file_id = message.document.file_id
        filename = message.document.file_name
    else:
        bot.reply_to(message, "⚠️ Please send a valid video file.")
        return

    # Download the file
    file_info = bot.get_file(file_id)
    downloaded = bot.download_file(file_info.file_path)
    with open(filename, "wb") as f:
        f.write(downloaded)

    # Extract audio
    audio_path = f"{message.from_user.id}_video_audio.mp3"
    videoclip = VideoFileClip(filename)
    videoclip.audio.write_audiofile(audio_path)

    # Convert audio to text
    segments, info = model.transcribe(audio_path, vad_filter=True)
    audio_text = " ".join(seg.text.strip() for seg in segments)

    # Reply safely
    reply = gpt_response(audio_text)
    send_long_message(bot, message.chat.id, f"🤖 GPT:\n{reply}")


# ===== بدء الدردشة =====
@bot.message_handler(commands=['chat'])
def send_welcome(message):
    bot.send_message(message.chat.id, "اختر نوع التفاعل:", reply_markup=main_chat_menu())

# ===== التعامل مع أزرار الدردشة =====
@bot.callback_query_handler(func=lambda call: call.data in markup_chat_data())
def handle_menu(call):
    if call.data == "chat_text":
        msg = bot.send_message(call.message.chat.id, "📝 اكتب النص الذي تريده:")
        bot.register_next_step_handler(msg, lambda m: process_text(bot, m))
    elif call.data == "chat_file":
        msg = bot.send_message(call.message.chat.id, "📂 أرسل الملف الآن:")
        bot.register_next_step_handler(msg, lambda m: process_file(bot, m))
    elif call.data == "chat_audio":
        msg = bot.send_message(call.message.chat.id, "🎙️ أرسل رسالة صوتية الآن:")
        bot.register_next_step_handler(msg, lambda m: process_audio(bot, m))
    elif call.data == "chat_video":
        bot.send_message(call.message.chat.id, "⚠️ ميزة الفيديو غير مفعلة حالياً.")
