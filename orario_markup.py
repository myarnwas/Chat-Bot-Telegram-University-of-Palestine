from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ============================
# MAIN MENU (Academic Programs)
# ============================
def markup_orario_cc():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("📘 متطلبات الجامعة", callback_data="o_up_univ"),
        InlineKeyboardButton("🦷 طب وجراحة الفم والأسنان", callback_data="o_up_dentistry"),
        InlineKeyboardButton("💊 الصيدلة", callback_data="o_up_pharmacy"),
        InlineKeyboardButton("🏗️ الهندسة", callback_data="o_up_engineering"),
        InlineKeyboardButton("🤖 الذكاء الاصطناعي", callback_data="o_up_ai"),
        InlineKeyboardButton("📰 الإعلام", callback_data="o_up_media"),
        InlineKeyboardButton("💻 تكنولوجيا المعلومات", callback_data="o_up_it"),
        InlineKeyboardButton("⚖️ القانون – عربي", callback_data="o_up_law_ar"),
        InlineKeyboardButton("⚖️ القانون – إنجليزي", callback_data="o_up_law_en"),
        InlineKeyboardButton("💼 إدارة المال والأعمال – عربي", callback_data="o_up_ba_ar"),
        InlineKeyboardButton("💼 إدارة المال والأعمال – إنجليزي", callback_data="o_up_ba_en"),
        InlineKeyboardButton("🎓 التربية", callback_data="o_up_edu"),
        InlineKeyboardButton("📜 الدبلوم المتوسط", callback_data="o_up_diploma"),
    )
    return markup


def markup_orario_cc_data():
    return [
        "o_up_univ",
        "o_up_dentistry",
        "o_up_pharmacy",
        "o_up_engineering",
        "o_up_ai",
        "o_up_media",
        "o_up_it",
        "o_up_law_ar",
        "o_up_law_en",
        "o_up_ba_ar",
        "o_up_ba_en",
        "o_up_edu",
        "o_up_diploma"
    ]
