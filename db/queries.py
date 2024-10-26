CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS store (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name varchar(255),
        category varchar(255),
        size varchar(255),
        price INTEGER,
        article varchar(255),
        photo varchar(255)
    )
"""

INSERT_PRODUCT_QUERY = """
    INSERT INTO store (product_name, category, size, price, article, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""

GET_PRODUCTS_QUERY = """
    SELECT * FROM store
"""