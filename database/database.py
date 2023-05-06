import pymysql
from pymysql import cursors

from config import *


def get_connection():
    try:
        connection = pymysql.connect(
            host="127.0.0.1" if DB_HOST == 'localhost' else DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=cursors.DictCursor
        )
        print('Successfully connected...')
        print('#' * 30)
        return connection
    except Exception as e:
        print('Connection refused...')
        print(e)
        print('#' * 30)
