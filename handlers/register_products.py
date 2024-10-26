from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff, bot
from db import db_main

class FSM_store(StatesGroup):
    product_name = State()
    category = State()
    size = State()
    price = State()
    article = State()
    photo = State()
    

async def start_insert_product(message : types.Message):
    await message.reply("Введите название продукта: ")
    await FSM_store.product_name.set()

async def get_product_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await message.answer("Введите категорию: ")
    await FSM_store.next()

async def get_category(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer("Введите размер:")
    await FSM_store.next()
    
async def get_size_product(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer("Введите цену:")
    await FSM_store.next()
    

async def get_price(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    await message.answer("Введите артикул товара: ")
    await FSM_store.next()

async def get_article_product(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text
    await message.answer("Отправьте фото товара")
    await FSM_store.next()
    
async def get_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer("Готово!")
    await db_main.insert_store(data['product_name'], data['category'], data['size'], data['price'], data['article'], data['photo'])
    await state.finish()

async def output_store(message : types.Message):
    products = await db_main.fetch_all_products()
    for product in products:
        await message.answer_photo(photo=product['photo'], 
                                   caption=f'name : {product['product_name']}'
                                   f'category : {product['category']}'
                                   f'price : {product['price']}'
                                   f'size : {product['size']}'
                                   f'article : {product['article']}'
                                   )

class get_store(StatesGroup):
    article = State()
    size = State()
    count = State()
    number = State()


async def start_get_product(message : types.Message):
    await message.answer("Введите артикул товара: ")
    await get_store.article.set()

async def get_article(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['article'] = message.text
    await message.answer("Введите размер: ")
    await get_store.next()

async def get_size(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer("Введите количество: ")
    await get_store.next()

async def get_count(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['count'] = message.text
    await message.answer("Оставьте свой номер для связи: ")
    await get_store.next()

async def get_number(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
    await message.answer("Готово скоро отправим товар")
    for i in staff:
        await bot.send_message(chat_id= i ,text = f"article : {data['article']}"
                               f"size : {data['size']}"
                               f"count : {data['count']}"
                               f"number : {data['number']}"
                               )

def filter_staff(message : types.Message):
    if message.from_user.id in staff:
        return True
    else:
        return False

def register_store(dp : Dispatcher):
    dp.register_message_handler(start_insert_product, filter_staff, commands=['store'])
    dp.register_message_handler(get_product_name, state=FSM_store.product_name)
    dp.register_message_handler(get_category, state=FSM_store.category)
    dp.register_message_handler(get_size_product, state=FSM_store.size)
    dp.register_message_handler(get_price, state=FSM_store.price)
    dp.register_message_handler(get_article_product, state=FSM_store.article)
    dp.register_message_handler(get_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(start_get_product, commands=['products'])
    dp.register_message_handler(get_article, state = get_store.article)
    dp.register_message_handler(get_size, state = get_store.size)
    dp.register_message_handler(get_count, state = get_store.number)
    dp.register_message_handler(get_number, state = get_store.number)
