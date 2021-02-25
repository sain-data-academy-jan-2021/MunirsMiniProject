import print_functions
import pymysql
import menu_functions
import validation_functions
from prettytable import from_db_cursor
import os

def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

def delete_product_in_db(connection):
    product_ids = [id[0] for id in execute_sql_select(connection, 'select product_id from products')]
    while True:
        print_functions.read_product_data_from_db(connection)
        id = validation_functions.getInteger("What product would you like to delete? Press 0 to cancel!")
        if id in product_ids:
            sql = (f'DELETE FROM products WHERE product_id = "{id}"')
            execute_sql(connection, sql)
        elif id == 0:
            break
        else:
            print("This product does not exist, please try again!")

def add_product_in_db(connection):
    product_names = [name[0] for name in execute_sql_select(connection, 'select product_name from products')]
    while True:
        print_functions.read_product_data_from_db(connection)
        name = input("What product would you like to add? (Press 0 to cancel!)").capitalize()
        if name in product_names:
            print("This product already exists, please try again!")
        elif name == "0":
            break
        else:
            new_product_price = validation_functions.getFloat("What is the price of the product you would you like to add? (Press 0 to cancel")
            sql = (f'INSERT INTO products (product_name, product_price) VALUES ("{name}", {new_product_price})')
            execute_sql(connection, sql)

def update_product_in_db(connection):
    product_ids = [id[0] for id in execute_sql_select(connection, 'select product_id from products')]
    while True:
        print_functions.read_product_data_from_db(connection)
        id = validation_functions.getInteger("What product would you like to update? Press 0 to cancel!")
        if id in product_ids:
            new_product_name = input("What is the new product you would like to add?")
            new_product_price = validation_functions.getFloat("What is the price of the new product?")
            sql = (f'UPDATE products SET product_name = "{new_product_name}", product_price = "{new_product_price}" WHERE product_id = "{id}"')
            execute_sql(connection, sql)
        elif id == 0:
            break
        else:
            print("This product does not exist, please try again!")

def add_courier_to_db(connection):
    courier_names = [name[0] for name in execute_sql_select(connection, 'select courier_name from couriers')]
    while True:
        print_functions.read_courier_data_from_db(connection)
        name = input("What is the name of the courier you would like to add? Press 0 to cancel!").capitalize()
        if name in courier_names:
            print("This courier already exists, please try again!")
        elif name == "0":
            break
        else:
            new_courier_phone = input("What is the phone number of the courier you would like to add?")
            sql = (f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("{name}", {new_courier_phone})')
            execute_sql(connection, sql)

def delete_courier_in_db(connection):
    courier_ids = [id[0] for id in execute_sql_select(connection, 'select courier_id from couriers')]
    while True:
        print_functions.read_courier_data_from_db(connection)
        id = validation_functions.getInteger("What courier would you like to delete? Press 0 to cancel!")
        if id in courier_ids:
            sql = (f'DELETE FROM couriers WHERE courier_id = "{id}"')
            execute_sql(connection, sql)
        elif id == 0:
            break
        else:
            print("This courier does not exist, please try again!")

def update_courier_in_db(connection):
    # courier_ids = [id[0] for id in execute_sql_select(connection, 'select courier_id from couriers')]
    # while True:
    #     print_functions.read_courier_data_from_db(connection)
    #     id = validation_functions.getInteger("What courier would you like to update? Press 0 to cancel")
    #     if id in courier_ids:
    print_functions.read_courier_data_from_db(connection)
    new_courier_name = input("What is the name of the new courier you would like to add?")
    new_courier_phone = input("What is the new phone number of the courier?")
    sql = (f'UPDATE couriers SET courier_name = "{new_courier_name}", courier_phone = "{new_courier_phone}" WHERE courier_id = "{id}"') 
    execute_sql(connection, sql)
        # elif id == 0:
        #     break
        # else:
        #     print("This courier does not exist, please try again!")


def delete_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        print_functions.read_order_data_from_db(connection)
        id = validation_functions.getInteger("What order would you like to delete from the list above? Press 0 to cancel")
        if id in existing_ids:
            execute_sql(connection, f'DELETE from basket where order_id = {id}')
            execute_sql(connection, f'DELETE from orders where order_id = {id}')
            break
        elif id == 0:
            break  
        else:
            print("This order does not exist, please try again!")

def add_order_to_db(connection):
    existing_names = [name[0] for name in execute_sql_select(connection, 'select customer_name from orders')]
    while True:
        print_functions.read_order_data_from_db(connection)
        name = input('Please enter your full name for the order, press 0 to cancel! \n').capitalize()
        if name in existing_names:
            print("This customer already exists, please try again")
        elif name == "0":
            break
        else:
            customer_address = input('Please enter a delivery address \n')
            customer_phone = input('Enter your phone number \n')
            courier = add_courier_to_order(connection)
            order_status = 'In progress'
            items = add_products_to_order(connection)
            execute_sql(connection, f"insert into orders (customer_name, customer_address, customer_phone, courier, order_status) values ('{name}', '{customer_address}', '{customer_phone}', '{courier}', '{order_status}')")
            order_id = execute_sql_select(connection, 'SELECT max(order_id) from orders')[0][0]
            for item in items:
                execute_sql(connection, f"insert into basket (order_id, product_id) values ({order_id}, {item})")

def update_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        print_functions.read_order_data_from_db(connection)
        id = validation_functions.getInteger("What order would you like to update from the list above? Press 0 to cancel")
        if id in existing_ids:
            updated_order_name = input("Please enter the updated name")
            updated_order_address = input("Please eneter the updated address")
            updated_phone = input("Please enter the updated phone number")
            print_functions.read_courier_data_from_db(connection)
            updated_courier = input("Please enter the updated courier from the list above")
            updated_status = input("Please enter the updated status of the order")
            execute_sql(connection, f'UPDATE orders SET customer_name = "{updated_order_name}", customer_address = "{updated_order_address}", customer_phone = "{updated_phone}", courier = "{updated_courier}", order_status = "{updated_status}" WHERE order_id = {id}')
            execute_sql(connection, f'DELETE from basket where order_id = {id}')
            items = add_products_to_order(connection)
            for item in items:
                execute_sql(connection, f"insert into basket (order_id, product_id) values ({id}, {item})")
            break
        elif id == 0:
            break
        else:
            print("This order does not exist, please try again!")

def update_order_status_in_db(connection):
    print_functions.read_order_data_from_db(connection)
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        id = validation_functions.getInteger("Which order's status would you like to update? Press 0 to cancel!")
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order?")
            execute_sql(connection, f'UPDATE orders SET order_status = "{updated_order_status}"')
            break
        elif id == 0:
            break
        else:
            print("This order does not exist, please try again!")


def add_courier_to_order(connection):
    print_functions.read_courier_data_from_db(connection)
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = validation_functions.getInteger("Which courier would you like to choose? Press 0 to cancel")
        if pick_courier in existing_ids:
            return pick_courier
        elif pick_courier == 0:
            break
        else:
            continue

def add_products_to_order(connection):
    print_functions.read_product_data_from_db(connection)
    existing_ids = []
    chosen_products = []
    for row in execute_sql_select(connection, 'SELECT product_id FROM products'):
        existing_ids.append(row[0])
    while True:
        pick_products = validation_functions.getInteger("What products would you like to add? Press 0 to coninue!")
        if pick_products in existing_ids:
            chosen_products.append(pick_products)
            continue
        elif pick_products == 0:
            break
        else:
            continue
    return chosen_products