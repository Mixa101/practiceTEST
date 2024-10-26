from aiogram import executor
import logging
from config import dp
from handlers import start_handler, register_products
from db.db_main import sql_create

async def on_startup(_):
    await sql_create()

start_handler.register_start_handlers(dp)
register_products.register_store(dp)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)