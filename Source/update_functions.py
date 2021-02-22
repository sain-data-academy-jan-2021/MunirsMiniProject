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

# Database Functions ----------------------------------------------------------------------------------------------------

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

def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

def delete_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        print_functions.read_order_data_from_db(connection)
        id = int(input("What order would you like to delete from the list above?"))
        if id in existing_ids:
            execute_sql(connection, f'DELETE from basket where order_id = {id}')
            execute_sql(connection, f'DELETE from orders where order_id = {id}')
            break  
        else:
            print("This option is invalid")

def add_order_to_db(connection):
    customer_name = input('Please enter your full name for the order \n').capitalize()
    customer_address = input('Please enter a delivery address \n')
    customer_phone = input('Enter your phone number \n')
    courier = add_courier_to_order(connection)
    order_status = 'In progress'
    items = add_products_to_order(connection)
    execute_sql(connection, f"insert into orders (customer_name, customer_address, customer_phone, courier, order_status) values ('{customer_name}', '{customer_address}', '{customer_phone}', '{courier}', '{order_status}')")
    order_id = execute_sql_select(connection, 'SELECT max(order_id) from orders')[0][0]
    for item in items:
        execute_sql(connection, f"insert into basket (order_id, product_id) values ({order_id}, {item})")

def update_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    chosen_products = [id[0] for id in execute_sql_select(connection, 'select product_id from products')]
    while True:
        print_functions.read_order_data_from_db(connection)
        id = int(input("What order would you like to update from the list above?"))
        if id in existing_ids:
            updated_order_name = input("Please enter the updated name")
            updated_order_address = input("Please eneter the updated address")
            updated_phone = input("Please enter the updated phone number")
            print_functions.read_courier_data_from_db(connection)
            updated_courier = input("Please enter the updated courier from the list above")
            updated_status = input("Please enter the updated status of the order")
            execute_sql(connection, f'UPDATE orders SET customer_name = "{updated_order_name}", customer_address = "{updated_order_address}", customer_phone = "{updated_phone}", courier = "{updated_courier}", order_status = "{updated_status}"')
            print_functions.read_product_data_from_db(connection)
            while True:
            execute_sql(connection, f'DELETE product_id FROM basket where order_id = {id}')
            updated_items = int(input("Please enter the new items you would like to add to the order, Press 0 to continue"))
                execute_sql(connection, f'UPDATE basket SET product_id = {updated_items} WHERE order_id = {id}')
                continue
                break
        #Delete from basket where order_id matches 
        
        #insert all new basket items for order
        
        
    for row in execute_sql_select(connection, 'SELECT product_id FROM basket W'):
        existing_ids.append(row[0])
    while True:
        updated_items = int(input("Please enter the new items you would like to add to the order, Press 0 to continue"))
        if updated_items in chosen_products:
            chosen_products.append(updated_items)
            execute_sql(connection, f'UPDATE basket SET product_id = {updated_items} WHERE order_id = {id}')
            continue
        elif updated_items == 0:
            break

def update_order_status_in_db(connection):
    print_functions.read_order_data_from_db(connection)
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        id = int(input("What order's status would you like to update?"))
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order?")
            execute_sql(connection, f'UPDATE orders SET order_status = "{updated_order_status}"')
            break


def add_courier_to_order(connection):
    print_functions.read_courier_data_from_db(connection)
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = int(input("What courier would you like to choose?"))
        if pick_courier in existing_ids:
            return pick_courier
        else:
            continue

def add_products_to_order(connection):
    print_functions.read_product_data_from_db(connection)
    existing_ids = []
    chosen_products = []
    for row in execute_sql_select(connection, 'SELECT product_id FROM products'):
        existing_ids.append(row[0])
    while True:
        pick_products = int(input("What products would you like to add? Press 0 to exit"))
        if pick_products in existing_ids:
            chosen_products.append(pick_products)
            continue
        elif pick_products == 0:
            break
        else:
            continue
    return chosen_products

#Delete from basket first then orders table