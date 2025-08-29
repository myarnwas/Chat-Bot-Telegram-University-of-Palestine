import telebot
from sedute.sedute_markup import *

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)


def sedute_1(message):
    bot.send_message(
        message.chat.id,
        "🎓 اختر الكلية/الخطة الدراسية لعرض الملفات:",
        reply_markup=markup_sedute()
    )

def callback_sedute_1(call):
    match call.data:
        case "sedute_dentistry":
            bot.send_document(call.from_user.id, open("./sedute/file/طب الأسنان.pdf", "rb"), timeout=120)
        case "sedute_pharmacy":
            bot.send_document(call.from_user.id, open("./sedute/file/خطة صيدلة.pdf", "rb"), timeout=120)
            bot.send_document(call.from_user.id, open("./sedute/file/خطة دكتور صيدلي.pdf", "rb"), timeout=120)
        case "sedute_ai":
            bot.send_document(call.from_user.id, open("./sedute/file/خطة الذكاء الاصطناعي.pdf", "rb"), timeout=120)
            bot.send_document(call.from_user.id, open("./sedute/file/software-plan.pdf", "rb"), timeout=120)
        case "sedute_it":
            bot.send_document(call.from_user.id, open("./sedute/file/تكنولوجيا المعلومات.pdf", "rb"))
        case "sedute_law_ar":
            bot.send_document(call.from_user.id, open("./sedute/file/القانون.pdf", "rb"))
        case "sedute_ba_ar":
            bot.send_document(call.from_user.id, open("./sedute/file/إدارة أعمال.pdf", "rb"))
