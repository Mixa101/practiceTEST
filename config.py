from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('BOT_TOKEN')
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage)
staff = []
