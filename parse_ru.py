from ast import parse
from time import sleep
import requests
from bs4 import BeautifulSoup as BS
from aiogram import types, Bot, Dispatcher, executor
import signal
import os

def signal_handler(sig, frame):
    print("Выход...")
    os.kill(os.getpid(), signal.SIGTERM)

token = '6442961458:AAHSzpstZC7BgImelYPbuRSk3vQeJ_uzwG8'

bot = Bot(token)
dp = Dispatcher(bot)

def get_ru(word):
    try:
        r = requests.get(f'https://fonetika.su/?word={word}')
        soup = BS(r.content, 'html.parser')
        return soup.find('div', class_='tabs_block').find('p').get_text()
    except Exception as e:
        return e
    
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer(f'Привет `{message.from_user.id}`', parse_mode='MarkdownV2')

@dp.message_handler()
async def get_word(message: types.Message):
    await message.answer(f'`{get_ru(message.text)}`', parse_mode='MarkdownV2')
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
            
        except Exception as e:
            print(e)
            sleep(240)