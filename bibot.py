import logging
import os
from transliterate import translit


from aiogram import Bot, Dispatcher
from aiogram.types import Message       
from aiogram.filters.command import Command 

bot = Bot(token='7536963923:AAHKGd-wAkTs5bt0RaTC1NxImSGyVgvezvQ')                        
dp = Dispatcher()                           
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
     user_name = message.from_user.full_name
     user_id = message.from_user.id
     text = f'Привет, {user_name}!'
     logging.info(f'{user_name} {user_id} запустил бота')
     await bot.send_message(chat_id=user_id, text=text)
     
@dp.message()
async def trans(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text 
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(translit(text, 'ru',reversed=True))
    
if __name__ == '__main__':
    logging.info("Бот запущен")
    dp.run_polling(bot)
     
