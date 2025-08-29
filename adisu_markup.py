from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def markup_adisu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("💵 الرسوم الدراسية", callback_data="a_fees"),
        InlineKeyboardButton("📝 إجراءات التسجيل", callback_data="a_registration"),
        InlineKeyboardButton("📅 التقويم الأكاديمي", callback_data="a_calendar"),
        InlineKeyboardButton("🧾 المنح والإعفاءات", callback_data="a_scholarship"),
        InlineKeyboardButton("❓ الدعم والاستفسارات", callback_data="a_support")
    )
    return markup


def markup_adisu_data():
    return ["a_fees", "a_registration", "a_calendar", "a_scholarship", "a_support"]
