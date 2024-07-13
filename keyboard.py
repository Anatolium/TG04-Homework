from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ----------------------------------- TG04-1. Создание простого меню с кнопками -----------------------------------
labels = ["Привет", "Пока"]


async def reply_keyboard():
    buttons = [KeyboardButton(text=label) for label in labels]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
    return keyboard


# ----------------------------------- TG04-2. Кнопки с URL-ссылками -----------------------------------------------

inline_keyboard_urls = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://mediametrics.ru/rating/hitech/ru/hour.html")],
    [InlineKeyboardButton(text="Музыка", url="https://youtu.be/-GfaQzgnnDI?si=M9Q9o0H4LsjLbzTQ&t=11")],
    [InlineKeyboardButton(text="Видео", url="https://youtube.com/shorts/4eNlzwOhH_w?si=7SYEl1-0FWAaundS")]
])

# ----------------------------------- TG04-3. Динамическое изменение клавиатуры -----------------------------------
inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='options')],
])

options = [["Опция 1", "option_1"], ["Опция 2", "option_2"]]


async def inline_keyboard_options():
    keyboard = InlineKeyboardBuilder()
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option[0], callback_data=option[1]))
    return keyboard.adjust(2).as_markup()
