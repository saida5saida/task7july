import psycopg2


# task 1
connection = psycopg2.connect(
    user = 'postgres',
    password = '',
    host = '',
    port = '',
    database = 'movie_db'
)

cursor = connection.cursor()
query = """
CREATE TABLE film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    FOREIGN KEY(genre_id),
    view_count INT DEFAULT 0,
    release_date DATE,
    has_fragman BOOLEAN DEFAULT false,
)
"""
# cursor.execute(query)
# connection.commit()

# task 2 
cursor = connection.cursor()
query = """
CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR NOT NULL,
    stock_count INT DEFAULT 0,
    is_fresh BOOLEAN DEFAULT true,
    FOREIGN KEY(seller_id),
    product_placement_date DATE,
    product_placement_time TIME,
    expiry_date DATE,
    price NUMERIC NOT NULL,
    sold_count INT DEFAULT 0,
    product_barcode UNIQUE NOT NULL
)
"""
cursor.execute(query)
connection.commit()
