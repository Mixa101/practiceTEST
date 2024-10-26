from aiogram import Dispatcher, types

async def command_start(message : types.Message):
    user_name = message.from_user.full_name
    await message.reply(f"Привет {user_name}, Добро пожаловать")

async def command_info(message : types.Message):
    await message.answer("Этот бот предназначен для продажи товаров ну и покупки разумеется вы можете посмотреть все доступные товары по команде '/products'")

def register_start_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_info, commands=['info'])