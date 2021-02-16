import sys
import print_functions
import save_functions
import update_functions 
import menu_functions
import text_functions
import csv
import os
import pymysql

from dotenv import load_dotenv


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
  host,
  user,
  password,
  database
)


print("""
      
Welcome to the..
__________                   .___             __     _____                 
\______   \_______  ____   __| _/_ __   _____/  |_  /  _  \ ______ ______  
 |     ___/\_  __ \/  _ \ / __ |  |  \_/ ___\   __\/  /_\  \\____ \\____ \ 
 |    |     |  | \(  <_> ) /_/ |  |  /\  \___|  | /    |    \  |_> >  |_> >
 |____|     |__|   \____/\____ |____/  \___  >__| \____|__  /   __/|   __/ 
                              \/           \/             \/|__|   |__|     
""")


def RunApp(connection):
    user_input_main = menu_functions.main_menu()
    while user_input_main != "0":
        
        if user_input_main == "1":
            user_input_product = menu_functions.product_menu()
            
            while user_input_product != 5:
                
                if user_input_product == "1":
                    print_functions.read_product_data_from_db(connection)
                    
                elif user_input_product == "2":
                    update_functions.add_product_in_db(connection)
                    
                elif user_input_product == "3":
                    update_functions.update_product_in_db(connection)
                    
                elif user_input_product == "4":
                    print_functions.read_product_data_from_db(connection)
                    update_functions.delete_product_in_db(connection)
                    
                elif user_input_product == "5":
                    
                    break
                else:
                    print("Bye Bye")
                    sys.exit()
                user_input_product = menu_functions.product_menu() 
            user_input_main = menu_functions.main_menu()
        elif user_input_main == "2":
            user_input_courier = menu_functions.courier_menu()
            
            while user_input_courier != 5:
                
                if user_input_courier == "1":
                    print_functions.read_courier_data_from_db(connection)
                    
                elif user_input_courier == "2":
                    update_functions.add_courier_to_db(connection)
                    
                elif user_input_courier == "3":
                    print_functions.read_courier_data_from_db
                    update_functions.delete_courier_in_db(connection)
                    
                elif user_input_courier == "4":
                    update_functions.update_courier_in_db(connection)
                elif user_input_courier == "5":
                    break
                user_input_courier = menu_functions.courier_menu()
            user_input_main = menu_functions.main_menu()
        elif user_input_main == "3": ####################################################################################
            user_input_order = menu_functions.order_menu()
            
            while user_input_order != 6:
                
                if user_input_order == "1":
                    print_functions.print_list(orders)
                    
                elif user_input_order == "2":
                    new_order_name = input("Please enter the name of the customer: ")
                    new_order_phone = input("Please enter the phone number of the customer: ")
                    new_order_address = input("Please enter the address of the customer: ")
                    print("The available couriers are::")
                    new_order = {
                        "customer_name": new_order_name,
                        "customer_phone": new_order_phone,
                        "customer_address": new_order_address,
                        "courier": text_functions.courier_list_select()["index"],
                        "status": "Preparing",
                        "items": text_functions.product_list_select()["index"]
                        }
                        
                        
                    update_functions.add_dict_to_list(new_order, orders)
                    
                elif user_input_order == "3":
                    order_name = input("Whose order status would you like to update? Press 0 to cancel! ")
                    
                    if order_name == "0":
                        menu_functions.order_menu()
                        
                    for order in orders:
                    
                        if order['customer_name'] == order_name:
                            print("The current status of this order is: ")
                            print(order['status'])
                        
                    new_status = input("What is the new status of this order? ")
                    
                    for order in orders:
                        
                        if order['customer_name'] == order_name:
                            order['status'] = new_status
                            print("The new order status is: " + new_status)
                    print(orders)
                    
                elif user_input_order == "4":
                    
                    order_name = input("Whose order would you like to update? ")
                    
                    for order in orders:
                        
                        if order['customer_name'] == order_name:
                            while True:
                                new_order_name = input("Please enter the updated name of the customer: ")
                                if new_order_name != "":
                                    order['customer_name'] = new_order_name
                                new_order_phone = input("Please enter the updated phone number of the customer: ")
                                if new_order_phone != "":
                                    order['customer_phone'] = new_order_phone
                                new_order_address = input("Please enter the updated address of the customer: ")
                                if new_order_address != "":
                                    order['customer_address'] = new_order_address
                                print("The available couriers are:")
                                
                                text_functions.courier_list_select()
                                
                                order['status'] = "Preparing"
                                print("The available items are:")
                                text_functions.product_list_select()
                                
                                break
                                
                            
                elif user_input_order == "5":
                    order_name = input("Whose order would you like to delete? ")
                    
                    for order in orders:
                        
                        if order['customer_name'] == order_name:
                            
                            update_functions.delete_dict_in_list(order, orders)
                            
                elif user_input_order == "6":
                    break
                    menu_functions.main_menu()
                user_input_order = menu_functions.order_menu()
            user_input_main = menu_functions.main_menu()
        elif user_input_main == "4":
            print("Your data has been saved, you will now exit the app")
            # save_functions.save_dict_products_to_csv("products.csv", products)
            # save_functions.save_dict_couriers_to_csv("couriers.csv", couriers)
            save_functions.save_dict_to_csv("orders.csv", orders)
            connection.close()
            exit()
            
        elif user_input_main == "0":
            connection.close()
            # menu_functions.main_menu() 

RunApp(connection)

# Enter address as string (.split into objects)
# Refining functions
# print to a table (pip install pretty table)



