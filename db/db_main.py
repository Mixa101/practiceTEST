import queries
import sqlite3

db = sqlite3.connect('db/store.sqlite3')
db.row_factory = sqlite3.Row
cursor = db.cursor()

async def sql_create():
    if db:
        print("database is ready!")
    
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)

async def fetch_all_products():
    products = cursor.execute(queries.GET_PRODUCTS_QUERY).fetchall()
    products = [dict(product) for product in products]
    return products

async def insert_store(product_name, category, size, price, article, photo):
    cursor.execute(queries.INSERT_PRODUCT_QUERY, (product_name, category, size, price, article, photo))
    db.commit()

