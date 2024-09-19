from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from usersID import *

mRT = Router()
ed = EditID()

Ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запись на занятие', callback_data='Запись')],
    [InlineKeyboardButton(text='Расписание', callback_data='Расписание')],
    [InlineKeyboardButton(text='Цены', callback_data='Цены')],
    [InlineKeyboardButton(text='Направления', callback_data='Направления')],
    [InlineKeyboardButton(text='Как нас найти', callback_data='Как найти')],
    [InlineKeyboardButton(text='Тренеры', callback_data='Тренеры')],
    [InlineKeyboardButton(text='Правила и скидки', callback_data='Правила')],
    [InlineKeyboardButton(text='О нас', callback_data='О нас')]
])


@mRT.message(CommandStart())
async def menu(mess: Message):
    await mess.answer(text='''Привет! Мы студия Light pole dance. 
Хочешь научиться крутым трюкам, прокачать силу на pole dance, улучшить растяжку, или может научиться танцевать ? 
Тогда тебе к нам. Задавай свои вопросы и записывайся на занятие.''', reply_markup=Ikb)
    ed.newID(mess)
    