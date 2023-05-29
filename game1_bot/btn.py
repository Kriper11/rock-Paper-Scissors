from aiogram import types


async def choose_hand_btn():
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("👊", callback_data="hand:stone"),
        types.InlineKeyboardButton("✌️", callback_data="hand:scissors"),
        types.InlineKeyboardButton("🤚", callback_data="hand:paper"),
    )

    return btn

