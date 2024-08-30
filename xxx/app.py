import aiogram
import asyncio
from os import getenv
from aiogram import Bot, Dispatcher, F
from dotenv import find_dotenv, load_dotenv

from menu import mRT
from record import rRT
from schedule import sRT

load_dotenv(find_dotenv())

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()
dp.include_routers(mRT, rRT, sRT)

@dp.message(F.photo)
async def nnn(photo: aiogram.types.Message):
    id = photo.photo[-1].file_id
    print(id)

async def main():
    await bot.delete_webhook(True)
    await dp.start_polling(bot)
asyncio.run(main())