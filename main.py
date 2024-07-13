import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboards as kb

# lesson_TG04_bot
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    # await callback.message.answer('Вот свежие новости!')
    # await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.inline_keyboard_test)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard_inline())


@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку')


@dp.message(CommandStart())
async def start(message: Message):
    # "reply_markup" позволяет что-то дополнительно отобразить вместе с сообщением; в данном случае клавиатуру
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=await kb.test_keyboard_reply())
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.reply_keyboard_test)
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)


@dp.message(Command('help'))
async def f_help(message: Message):
    await message.answer(
        "Бот умеет выполнять команды:\n/start\n/help\n/minitraining")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
