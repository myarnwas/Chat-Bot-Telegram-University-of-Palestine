from random import choice
from chat.chat_markup import main_chat_menu, markup_chat_data
from chat.chat_function import process_text, process_file, process_audio, process_video
from orario.orario_functions import *
from adisu.adisu_functions import *
from sedute.sedute_functions import *
from Notifications import bot_notifications  # فقط للاستدعاء لتشغيله
import telebot
from telebot import types
import os
# my very secret (!) token is stored in a json file having this template:
# { "token" : "abc123abc123" }
import json
token_json = json.load(open("telegram_token.json"))
TOKEN = token_json["token"]


bot = telebot.TeleBot(TOKEN, parse_mode=None)
# chat_id = message.chat.id (int)
# chat_id = call.from_use.id (int)

bot.delete_my_commands(scope=None, language_code=None)
bot.set_my_commands(commands=[
        telebot.types.BotCommand("start", "ابدأ استخدام البوت"),
        telebot.types.BotCommand("orario", "📅 الجداول الدراسية والامتحانات"),
        telebot.types.BotCommand("howto", "ℹ️ كيف تستخدم البوت؟"),
        telebot.types.BotCommand("sedute", "🎓 جداول وخطط الكليات"),
        telebot.types.BotCommand("adisu", "❓ الأسئلة الشائعة والمنح"),
        telebot.types.BotCommand("chat", "💬 دردشة"),
        telebot.types.BotCommand("notifications", "🔔  تنبيهات ذكية"),
        telebot.types.BotCommand("close", "✖️ إنهاء البوت")
    ])


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome 👋 to the University of Palestine Academic Assistant Bot!\n\n"
        "I am here to provide quick and accurate answers to common student inquiries, "
        "such as course registration, exam schedules, and academic policies.\n\n"
        "Please use the menu below to select your query and get instant assistance.")


@bot.message_handler(commands=['getid'])
def get_chat_user_id(message):
    bot.send_message(message.chat.id, "Il tuo ID è: " + str(message.from_user.id))


@bot.message_handler(commands=['howto'])
def send_howto(message):
    github_link = "https://github.com/myarnwas/Chat-Bot-Telegram-University-of-Palestine/tree/main"
    bot.reply_to(message, f"📖 لمزيد من التفاصيل حول كيفية استخدام البوت، اقرأ ملف الـ README هنا:\n\n{github_link}")



# just for fun
@bot.message_handler(func=lambda m: "white" in m.text.lower())
def get_chat_user_id(message):
    bot.send_message(message.chat.id, "Lo sviluppatore 😎🦦🦍")


'''
# TEMPORARY rispondere al messaggio
@bot.message_handler(func=lambda m: m.content_type == "text" )
def prova_text(message):
    bot.reply_to(message, "Questo messaggio posso capirlo. \nIt is a " + message.content_type)
'''


# HANDLING NON-UNDERSTANDABLE MESSAGES
@bot.message_handler(content_types=["sticker", "location", "contact"])
def handle_non_understandable_message(message):
    bot.reply_to(message, choice([
        "❌ لا أفهم هذا النوع من الرسائل",
        "يمكنني التعامل فقط مع نصوص، ملفات، صوتيات وفيديوهات"
    ]))

########################################################################################################################
# ORARIO

# عرض القائمة عند كتابة /orario أو كلمة orario
@bot.message_handler(commands=["orario"])
@bot.message_handler(func=lambda m: "orario" in m.text.lower())
def message_handler_orario(message):
    orario_1(message)


# التعامل مع الضغط على أي زر من قائمة التخصصات
@bot.callback_query_handler(func=lambda call: call.data in markup_orario_cc_data())
def callback_orario(call):
    callback_orario_cc_1(call)

########################################################################################################################
# ADISU


@bot.message_handler(commands=["adisu"])
def message_handler_adisu(message):
    adisu_1(message)


@bot.callback_query_handler(func=lambda call: call.data in markup_adisu_data())
def callback_adisu_quest(call):
    callback_adisu_quest_1(call)


########################################################################################################################
@bot.message_handler(func=lambda m: "sedute" in m.text.lower())
@bot.message_handler(commands=["sedute"])
def message_handler_sedute_di_laurea(message):
    sedute_1(message)


@bot.callback_query_handler(func=lambda call: call.data in markup_sedute_data())
def callback_sedute(call):
    callback_sedute_1(call)

########################################################################################################################
# ===== دردشة بالـ InlineKeyboard =====

@bot.message_handler(commands=['chat'])
def send_welcome(message):
    bot.send_message(message.chat.id,"اختر نوع التفاعل:",
        reply_markup=main_chat_menu())
    



# ===== التعامل مع الضغط على الأزرار =====
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
        msg = bot.send_message(call.message.chat.id, "🎬 أرسل الفيديو الآن:")
        bot.register_next_step_handler(msg, lambda m: process_video(bot, m))

########################################################################################################################

# --- التعامل مع البند Notifications ---
@bot.message_handler(commands=['notifications'])

@bot.message_handler(func=lambda message: message.text == "🔔 Notifications")
def notifications_menu(message):
    bot_notifications.start_notifications(bot, message)  # ✅ استدعاء الدالة الصحيحة


# --- المعالج العام لباقي الرسائل ---
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # استثناء رسائل خيارات التنبيهات
    if message.text in ['✔️ تسجيل', '✔️ امتحانات', '✔️ رسوم', '✔️ كلهم']:
        return  # تجاهلها، لأنه bot_notifications بيتعامل معها
    bot.send_message(message.chat.id, f"لم يتم التعرف على الخيار: {message.text}")

########################################################################################################################
@bot.message_handler(commands=["close"])
def close_bot(message):
    bot.reply_to(message, "✅ تم إنهاء الجلسة. شكرًا لاستخدامك البوت ✨")
    bot.stop_polling()

bot.infinity_polling(timeout=60)

