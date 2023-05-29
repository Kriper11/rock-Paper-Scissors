import logging
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from btn import *
from aiogram.dispatcher import FSMContext

BOT_TOKEN = "6070005452:AAFNyX3sMYNd2cikE6q9omDqUynGA4xixG8"

logging.basicConfig(level=logging.INFO)

# bot = Bot(token=BOT_TOKEN, parse_mode='html')
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

info = {
    'name': "",
    'age': 0,
    'address': '',
}

class MeningStatlarim(StatesGroup):
    ism = State()
    yosh = State()
    address = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    btn = await start_menu_btn()
    await message.answer(f"Привет\n Ваш имя:{first_name}\n Ваше юзернейм:{username} ", reply_markup=btn,)


@dp.message_handler(text="👤 Свизатся с админом")
async def support_handler(message: types.Message):
    await message.answer("Админ бота: @Kreper11")


@dp.message_handler(text="📑 Пройти регистрацию")
async def user_register_handler(message: types.Message):
    await message.answer("Ведите имя: ")
    await MeningStatlarim.ism.set()


@dp.message_handler(state=MeningStatlarim.ism)
async def ism_state(message: types.Message):
    info['name'] = message.text

    await message.answer("Ведите возраст: ")
    await MeningStatlarim.yosh.set()


@dp.message_handler(state=MeningStatlarim.yosh)
async def yosh_state(message: types.Message):
    info['age'] = message.text

    await message.answer("Ведите адрес: ")
    await MeningStatlarim.address.set()


@dp.message_handler(state=MeningStatlarim.address)
async def address_state(message: types.Message, state: FSMContext):
    info['address'] = message.text

    btn = await info_yes_or_no_btn()
    await message.answer(f"ИМЯ: {info['name']}\nВОЗРАСТ: {info['age']}\nАДРЕС: {info['address']}", reply_markup=btn)

    await state.finish()


@dp.callback_query_handler(text='yes')
async def answer_yes_callback(call: types.CallbackQuery):
    # await call.answer("Вы прошли регистрацию", show_alert=True)
    btn = await start_menu_btn()
    await call.message.answer("Вы прошли регистрацию", reply_markup=btn)


@dp.callback_query_handler(text='no')
async def answer_no_callback(call: types.CallbackQuery):
    # await call.answer("Вы не согласны", show_alert=True)
    btn = await start_menu_btn()
    await call.message.answer("Вы не прошли регистрацию!", reply_markup=btn)
    
if __name__ == "__main__":
    executor.start_polling(dp)