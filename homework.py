import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboard as kb

# lesson_TG04_bot
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('help'))
async def f_help(message: Message):
    await message.answer(
        "Бот умеет выполнять команды:\n/start\n/help\n/links\n/dynamic")


# ----------------------------------- TG04-1. Создание простого меню с кнопками -----------------------------------
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Нажми на кнопку, {message.from_user.first_name}", reply_markup=await kb.keyboard_reply())


@dp.message(F.text == "Привет")
async def hi_button(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(F.text == "Пока")
async def by_button(message: Message):
    await message.answer(f"Пока, {message.from_user.first_name}")


# ----------------------------------- TG04-2. Кнопки с URL-ссылками -----------------------------------------------
@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_urls)


# ----------------------------------- TG04-3. Динамическое изменение клавиатуры -----------------------------------
@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f'Динамическая клавиатура', reply_markup=kb.inline_keyboard_dynamic)


@dp.callback_query(F.data == 'options')
async def options(callback: CallbackQuery):
    await callback.message.answer('Показываю больше:', reply_markup=await kb.keyboard_inline())


@dp.callback_query(F.data == 'option_1')
async def option_1(callback: CallbackQuery):
    await callback.message.answer("Ты выбрал опцию 1")


@dp.callback_query(F.data == 'option_2')
async def option_2(callback: CallbackQuery):
    await callback.message.answer("Ты выбрал опцию 2")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
