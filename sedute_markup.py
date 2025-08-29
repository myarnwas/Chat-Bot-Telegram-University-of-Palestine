from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def markup_sedute():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("🦷 طب الأسنان", callback_data="sedute_dentistry"),
        InlineKeyboardButton("💊 الصيدلة", callback_data="sedute_pharmacy"),
        InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="sedute_ai"),
        InlineKeyboardButton("💻 تكنولوجيا المعلومات", callback_data="sedute_it"),
        InlineKeyboardButton("⚖️ القانون – عربي", callback_data="sedute_law_ar"),
        InlineKeyboardButton("💼 إدارة المال والأعمال – عربي", callback_data="sedute_ba_ar"),
    )
    return markup

def markup_sedute_data():
    return [
        "sedute_dentistry", "sedute_pharmacy", 
        "sedute_ai", "sedute_it",
        "sedute_law_ar", "sedute_ba_ar"
    ]