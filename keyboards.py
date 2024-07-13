from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

reply_keyboard_test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"),
     KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

# inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Видео", url="https://youtu.be/Bg3pFjbCag0?si=KSi4f33ostJHRh8Z")]
# ])

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
    [InlineKeyboardButton(text="Новости", callback_data='news')],
    [InlineKeyboardButton(text="Профиль", callback_data='person')]
])

buttons = ["Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4"]


async def test_keyboard_reply():
    keyboard = ReplyKeyboardBuilder()
    for button in buttons:
        keyboard.add(KeyboardButton(text=button))
    # as_markup(): клавиатуру можно использовать для отправки сообщений
    return keyboard.adjust(2).as_markup()


async def test_keyboard_inline():
    keyboard = InlineKeyboardBuilder()
    for key in buttons:
        keyboard.add(InlineKeyboardButton(text=key, url='https://youtu.be/-GfaQzgnnDI?si=M9Q9o0H4LsjLbzTQ&t=11'))
    return keyboard.adjust(2).as_markup()
