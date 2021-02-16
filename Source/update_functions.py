import print_functions
import pymysql
import menu_functions

def update_item_in_list(item_old, item_new, list):
    if item_old in list:
        list.remove(item_old)
        list.append(item_new)
        print_functions.print_list(list)

def add_item_to_list(item, list):
    list.append(item)
    print_functions.print_list(list)

def delete_item_in_list(item, list):
    if item in list:
        list.remove(item)
        print_functions.print_list(list)

def delete_dict_in_list(dict, list):
    if dict in list:
        list.remove(dict)

def add_dict_to_list(dict, list):
    list.append(dict)
    

def update_dict_in_list(dict_old, dict_new, list):
    if dict_old in list:
        list.remove(dict_old)
        list.append(dict_new)
        print_functions.print_list(list)

def delete_product_in_db(connection):
    delete_product = int(input("What product would you like to delete? (Press 0 to cancel!)"))
    if delete_product == "0":
        return
    sql = (f'DELETE FROM products WHERE product_id = "{delete_product}"')
    execute_sql(connection, sql)
    
def add_product_in_db(connection):
    new_product_name = input("What product would you like to add? (Press 0 to cancel!) ")
    if new_product_name == "0":
        return
    new_product_price = float(input("What is the price of this product?"))
    if new_product_price == "0":
        return
    sql = (f'INSERT INTO products (product_name, product_price) VALUES ("{new_product_name}", {new_product_price}')
    execute_sql(connection, sql)

def update_product_in_db(connection):
    print_functions.read_product_data_from_db(connection)
    product_id = int(input("What product would you like to update? (Press 0 to cancel!)"))
    if product_id == "0":
        return
    new_product_name = input("What is the new product you would like to add?")
    new_product_price = float(input("What is the price of the product?"))
    sql = (f'UPDATE products SET product_name = "{new_product_name}", product_price = "{new_product_price}" WHERE product_id = "{product_id}"')
    execute_sql(connection, sql)

def add_courier_to_db(connection):
    new_courier_name = input("What is the name of the courier you would like to add?")
    new_courier_phone = input("What is the phone number of the courier you would like to add?")
    sql = (f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("{new_courier_name}", {new_courier_phone})')
    execute_sql(connection, sql)

def delete_courier_in_db(connection):
    print_functions.read_courier_data_from_db(connection)
    delete_courier = int(input("Which courier would you like to delete? (Press 0 to cancel!)"))
    sql = (f'DELETE FROM couriers WHERE courier_id = "{delete_courier}"')
    execute_sql(connection, sql)

def update_courier_in_db(connection):
    print_functions.read_courier_data_from_db(connection)
    courier_id = int(input("What courier would you like to update? (Press 0 to cancel!)"))
    if courier_id == 0:
        return
    new_courier_name = input("What is the name of the new courier you would like to add?")
    new_courier_phone = input("What is the new phone number of the courier?")
    sql = (f'UPDATE couriers SET courier_name = "{new_courier_name}", courier_phone = "{new_courier_phone}" WHERE courier_id = "{courier_id}"') 
    execute_sql(connection, sql)

def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

