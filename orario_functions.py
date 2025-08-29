import telebot
from orario.orario_markup import *

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)


########################################################################################################################
# إرسال رابط الجدول مباشرة
def send_exam_schedule(call, program_name, url):
    bot.send_message(call.from_user.id, f"📚 جدول الامتحانات لقسم *{program_name}* ⬇️\n{url}", parse_mode="Markdown")
    bot.delete_message(call.from_user.id, call.message.message_id)


########################################################################################################################
# Main Menu
def orario_1(message):
    bot.send_message(
        message.chat.id,
        "اختر تخصصك لعرض جدول الامتحانات 📅:",
        reply_markup=markup_orario_cc()
    )


########################################################################################################################
# Callback Handlers

def callback_orario_cc_1(call):
    match call.data:
        case "o_up_univ":
            send_exam_schedule(call, "متطلبات الجامعة", "https://go.up.edu.ps/djori7")
        case "o_up_dentistry":
            send_exam_schedule(call, "طب وجراحة الفم والأسنان", "https://go.up.edu.ps/bitv79")
        case "o_up_pharmacy":
            send_exam_schedule(call, "الصيدلة", "https://go.up.edu.ps/9ooac3")
        case "o_up_engineering":
            send_exam_schedule(call, "الهندسة", "https://go.up.edu.ps/t5r2ks")
        case "o_up_ai":
            send_exam_schedule(call, "الذكاء الاصطناعي", "https://go.up.edu.ps/3oqbyt")
        case "o_up_media":
            send_exam_schedule(call, "الإعلام", "https://go.up.edu.ps/uoigdy")
        case "o_up_it":
            send_exam_schedule(call, "تكنولوجيا المعلومات", "https://go.up.edu.ps/694x5w")
        case "o_up_law_ar":
            send_exam_schedule(call, "القانون – عربي", "https://go.up.edu.ps/f575x3")
        case "o_up_law_en":
            send_exam_schedule(call, "القانون – إنجليزي", "https://go.up.edu.ps/l1efta")
        case "o_up_ba_ar":
            send_exam_schedule(call, "إدارة المال والأعمال – عربي", "https://go.up.edu.ps/5tx6mw")
        case "o_up_ba_en":
            send_exam_schedule(call, "إدارة المال والأعمال – إنجليزي", "https://go.up.edu.ps/ai70va")
        case "o_up_edu":
            send_exam_schedule(call, "التربية", "https://go.up.edu.ps/tcc8wf")
        case "o_up_diploma":
            send_exam_schedule(call, "الدبلوم المتوسط", "https://go.up.edu.ps/1axc2j")
