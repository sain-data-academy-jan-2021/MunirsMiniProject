import pymysql
import menu_functions
import print_functions
import os
from prettytable import from_db_cursor

def read_product_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT product_id, product_name, product_price FROM products;')
    mytable = from_db_cursor(cursor)
    print(mytable)


def read_courier_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers;')
    mytable = from_db_cursor(cursor)
    print(mytable)


def read_order_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders;')
    mytable = from_db_cursor(cursor)
    print(mytable)
