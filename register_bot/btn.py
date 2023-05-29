from aiogram import types


async def start_menu_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.KeyboardButton("📑 Пройти регистрацию"),
        types.KeyboardButton("👤 Свизатся с админом"),
    )
    return btn


async def info_yes_or_no_btn():
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("yes", callback_data="yes"),
        types.InlineKeyboardButton("no", callback_data="no"),
    )
    return btn






