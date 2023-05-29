import logging

from aiogram import Bot, Dispatcher, executor, types
from btn import choose_hand_btn
import random


logging.basicConfig(level=logging.INFO)

BOT_TOEKN = '5816510725:AAGNBe0dYyPomB_KM44QrmbQ5rFanFPh3vk'
bot = Bot(token=BOT_TOEKN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

hands = ["stone", "scissors","paper"]
hands_emoji = {
    "stone": "👊",
    "scissors": "✌️",
    "paper": "🤚",
}
bot_choose = ''


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    await message.answer("O`yin botimizga xush kelibsiz!\n\nO`yini boshlash uchun /game komandasini kiriting")


@dp.message_handler(commands=['game'])
async def start_game_handler(message: types.Message):
    global bot_choose
    btn = await choose_hand_btn()
    bot_choose = random.choice(hands)
    await message.answer("Tanlang: ", reply_markup=btn)


@dp.callback_query_handler(text_contains="hand:")
async def check_hands(call: types.CallbackQuery):
    user_choose = call.data.split(":")[1]
    # [hand, stone]
    # hand:stone

    if user_choose == bot_choose:
        await call.message.edit_text(f"Bir xil!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
    elif user_choose == 'stone':
        if bot_choose == 'scissors':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")

    elif user_choose == 'scissors':
        if bot_choose == 'paper':
            await call.message.edit_text(f"Siz yutingiz!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")
        else:
            await call.message.edit_text(f"Bot yuti!\n\nBOT: {hands_emoji[bot_choose]}\nSIZ: {hands_emoji[user_choose]}")



    


if __name__ == '__main__':
    executor.start_polling(dp)