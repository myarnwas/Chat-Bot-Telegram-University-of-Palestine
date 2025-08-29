# chat/chat_markup.py
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_chat_menu():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📝 نص", callback_data="chat_text"),
        InlineKeyboardButton("📂 ملف", callback_data="chat_file")
    )
    markup.row(
        InlineKeyboardButton("🎙️ صوت", callback_data="chat_audio"),
        InlineKeyboardButton("🎬 فيديو", callback_data="chat_video")
    )
    return markup

def markup_chat_data():
    return [
        "chat_text",
        "chat_file",
        "chat_audio",
        "chat_video"
    ]
