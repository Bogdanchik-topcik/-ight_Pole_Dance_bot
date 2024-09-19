from aiogram import Bot
from os import getenv
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
bot = Bot(token=getenv('TOKEN'))

usersID = {}

class EditID():

    def newID(_self_, mess):
        '''Создаю новый ключ id'''
        usersID[mess.chat.id] = [[], # messages id
                                 []  # direction id
                       ]


    def new_messID(_self_, mess):
        '''Новое id сообщения'''
        messID = int(mess.message_id)
        usersID[mess.chat.id][0].append(messID)


    def new_directionID(_self_, mess):
        '''Записывает id cообщения с направлением'''
        messID = int(mess.message_id)
        usersID[mess.chat.id][1].append(messID)


    async def del_directionID(_self_, chatID):
        '''Удаляет id сообщений'''
        messID = usersID[chatID][1]
        if messID:
            await bot.delete_messages(chat_id=chatID, message_ids=messID)
            usersID[chatID][1].clear()


    async def del_MessChat(_init_, chatID):
        '''Удаляет все сообщения присланные в чат бота'''

        messID = usersID[chatID][0] + usersID[chatID][1]
        if messID:
            await bot.delete_messages(chat_id=chatID, message_ids=messID)
            usersID[chatID] = [[],  # messages id
                               []]  # direction id