import pymysql
import menu_functions
import print_functions
import update_functions

def print_list(list):
    for item in list:
        print(item)

def read_product_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT product_id, product_name, product_price FROM products;')
    product_rows = cursor.fetchall()
    for row in product_rows:
        print(row)
    cursor.close()

def read_courier_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers;')
    courier_rows = cursor.fetchall()
    for row in courier_rows:
        print(row)
    cursor.close()


def read_order_data_from_db(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders;')
    order_rows = cursor.fetchall()
    for row in order_rows:
        print(row)
    cursor.close()

def delete_product_in_db(connection):
    delete_product = int(input("What product would you like to delete? (Press 0 to cancel!)"))
    if delete_product == "0":
        return
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM products WHERE product_id = "{delete_product}"')
    cursor.close()
    connection.commit()
    
def add_product_in_db(connection):
    new_product_name = input("What product would you like to add? (Press 0 to cancel!) ")
    if new_product_name == "0":
        return
    new_product_price = float(input("What is the price of this product?"))
    if new_product_price == "0":
        return
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO products (product_name, product_price) VALUES ("{new_product_name}", {new_product_price})')
    cursor.close()
    connection.commit()
    
def update_product_in_db(connection):
    cursor = connection.cursor()
    print_functions.read_product_data_from_db(connection)
    product_id = int(input("What product would you like to update? (Press 0 to cancel!)"))
    if product_id == "0":
        return
    new_product_name = input("What is the new product you would like to add?")
    new_product_price = float(input("What is the price of the product?"))
    cursor.execute(f'UPDATE products SET product_name = "{new_product_name}", product_price = "{new_product_price}" WHERE product_id = "{product_id}"')
    cursor.close()
    connection.commit()

def add_courier_to_db(connection):
    new_courier_name = input("What is the name of the courier you would like to add?")
    new_courier_phone = input("What is the phone number of the courier you would like to add?")
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("{new_courier_name}", {new_courier_phone})')
    cursor.close()
    connection.commit()

def delete_courier_in_db(connection):
    print_functions.read_courier_data_from_db(connection)
    delete_courier = int(input("Which courier would you like to delete? (Press 0 to cancel!)"))
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM couriers WHERE courier_id = "{delete_courier}"')
    cursor.close()
    connection.commit()

def update_courier_in_db(connection):
    cursor = connection.cursor()
    print_functions.read_courier_data_from_db(connection)
    courier_id = int(input("What courier would you like to update? (Press 0 to cancel!)"))
    new_courier_name = input("What is the name of the new courier you would like to add?")
    new_courier_phone = input("What is the new phone number of the courier?")
    cursor.execute(f'UPDATE couriers SET courier_name = "{new_courier_name}", courier_phone = "{new_courier_phone}" WHERE courier_id = "{courier_id}"')
    cursor.close()
    connection.commit()

