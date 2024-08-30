from os import getenv

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from db import new_mesidDB, give_mesidBD, del_mesidDB

rRT = Router()
bot = Bot(getenv('TOKEN'))


Ikb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Pole Dance Art утро (ВТ, ПТ - 8:45 )', callback_data='1')],
    [InlineKeyboardButton(text='Pole Dance Art вечер (ВТ, ПТ - 20:00)', callback_data='2')],
    [InlineKeyboardButton(text='Pole Sport начинающие (ПН, ЧТ - 18:30, ВС - 18:00 смешанная)', callback_data='3')],
    [InlineKeyboardButton(text='Pole Sport продолжающие (ПН, ЧТ - 19:30, ВС - 18:00 смешанная)', callback_data='4')],
    [InlineKeyboardButton(text='Pole Dance Choreo (ВС - 15:30)', callback_data='5')],
    [InlineKeyboardButton(text='Pole Dance Exotic (СР - 20:00, ВС - 16:30)', callback_data='6')],
    [InlineKeyboardButton(text='Stretching (ВТ 19:30, ПТ, ВС - 19:00)', callback_data='7')],
    [InlineKeyboardButton(text='Strip (СР 19:00, ВС 18:00)', callback_data='8')],
    [InlineKeyboardButton(text='Choreo (СР 20:00, ВС 12:00)', callback_data='9')],
    [InlineKeyboardButton(text='Salsation(ПН, ЧТ - 19:00)', callback_data='10')],
    [InlineKeyboardButton(text='Pole Sport с нуля (ВТ - 18:30, ПТ - 18.00)', callback_data='11')],
    [InlineKeyboardButton(text='Handstand (ВС - 17.00)', callback_data='12')],
    [InlineKeyboardButton(text='Не знаю, подскажите', callback_data='13')]
])

Rkb1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='пропустить')]
], resize_keyboard=True)

class recrd(StatesGroup):
    name = State()
    phone = State()
    direction = State()
    comment = State()


@rRT.callback_query(F.data == 'Запись')
async def records(call: Message, state: FSMContext): 


    await state.clear()
    await state.set_state(recrd.name)

    chatID = call.from_user.id
     # Работа с бд
    ID = give_mesidBD(chatID)
    if ID:
        await bot.delete_messages(chat_id=chatID, message_ids=ID)
        del_mesidDB(chatID)

    new_mesidDB(await call.message.answer("Введите имя"))
    await call.answer()

@rRT.message(recrd.name)
async def name(mess: Message, state: FSMContext):

    new_mesidDB(mess)

    await state.update_data(name=mess.text)
    await state.set_state(recrd.phone)

    new_mesidDB(await mess.answer("Введите свой номер телефона"))

@rRT.message(recrd.phone)
async def phone(mess: Message, state: FSMContext):

    new_mesidDB(mess)

    await state.update_data(phone=mess.text)
    await state.set_state(recrd.direction)

    new_mesidDB(await mess.answer("Выберете направление:", reply_markup=Ikb1))
    


@rRT.callback_query(recrd.direction)
async def diction(call: CallbackQuery, state: FSMContext):

    new_mesidDB(call.message)
    направления = {'1':'Pole Dance Art утро (ВТ, ПТ - 8:45 )','2':'Pole Dance Art вечер (ВТ, ПТ - 20:00)','3':'Pole Sport начинающие (ПН, ЧТ - 18:30, ВС - 18:00 смешанная)',
    '4':'Pole Sport продолжающие (ПН, ЧТ - 19:30, ВС - 18:00 смешанная)','5':'Pole Dance Choreo (ВС - 15:30)','6':'Pole Dance Exotic (СР - 20:00, ВС - 16:30)',
    '7':'Stretching (ВТ 19:30, ПТ, ВС - 19:00)','8':'Strip (СР 19:00, ВС 18:00)','9':'Choreo (СР 20:00, ВС 12:00)','10':'Salsation(ПН, ЧТ - 19:00)',
    '11':'Pole Sport с нуля (ВТ - 18:30, ПТ - 18.00)','12':'Handstand (ВС - 17.00)','13':'Не знаю, подскажите'}
    await state.update_data(direction=направления[call.data])
    await state.set_state(recrd.comment)

    new_mesidDB(await call.message.answer('Напишите комментарий или вопрос. если хотите пропустить, то нажмите "пропустить" ', reply_markup=Rkb1))
    await call.answer()


@rRT.message(recrd.comment)
async def comment(mess: Message, state: FSMContext):

    new_mesidDB(mess)

    await state.update_data(comment=mess.text)
    data = await state.get_data()
    await state.clear()
    # id = '5465180498'  # my
    id = '522687117'  # julia
    await bot.send_message(chat_id=id, text=f"{data['name']}")
    await bot.send_message(chat_id=id, text=f"{data['phone']}")
    await bot.send_message(chat_id=id, text=f"{data['direction']}")
    if data['comment'] != 'пропустить':
        await bot.send_message(chat_id=id, text=f"{data['comment']}")

    new_mesidDB(await mess.answer("Принято 👍", reply_markup=ReplyKeyboardRemove()))
    
