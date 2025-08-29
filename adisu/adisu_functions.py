import telebot
from telebot import formatting
from adisu.adisu_markup import *

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

def adisu_1(message):
    bot.send_message(
        message.chat.id,
        "📌 هذه قائمة بالأسئلة الشائعة لطلبة *جامعة فلسطين*.\n"
        "اضغط على الموضوع الذي تريد معرفته:",
        parse_mode="Markdown",
        reply_markup=markup_adisu()
    )

def callback_adisu_quest_1(call):
    match call.data:

        case "a_fees":
            bot.send_photo(call.from_user.id, open("./adisu/file/الرسوم_الدراسية.jpg", "rb"))

        case "a_registration":
            bot.send_photo(call.from_user.id, open("./adisu/file/اجراءات_التسجيل.jpg", "rb"))

        case "a_calendar":
            bot.send_photo(call.from_user.id, open("./adisu/file/التقويم_الاكاديمي.jpg", "rb"))

        case "a_scholarship":
            bot.send_message(call.from_user.id, "🔗 رابط المنح والإعفاءات: https://newstudent.up.edu.ps/schoolerships.php")

        case "a_support":
            bot.send_message(call.from_user.id, "🔗 الأسئلة الشائعة: https://up.edu.ps/ar/board/%D8%A7%D9%84%D8%B4%D8%A4%D9%88%D9%86_%D8%A7%D9%84%D8%A3%D9%83%D8%A7%D8%AF%D9%8A%D9%85%D9%8A%D8%A9/%D8%A7%D9%84%D9%86%D8%B8%D8%A7%D9%85_%D8%A7%D9%84%D8%A3%D9%83%D8%A7%D8%AF%D9%8A%D9%85%D9%8A")

    bot.delete_message(call.from_user.id, call.message.message_id)
