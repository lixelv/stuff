import time
import aiogram, aiogram.types
from parse import capture_full_page_screenshot, driver
from os import environ

token = environ['TELEGRAM']
bot = aiogram.Bot(token)

dp = aiogram.Dispatcher(bot)

@dp.message_handler
