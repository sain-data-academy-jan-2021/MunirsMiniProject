import sys
# import print_functions
# import save_functions
# import update_functions 
# import menu_functions
# import text_functions
# import csv
import pymysql
import os
import db_functions
from dotenv import load_dotenv

load_dotenv()

#12-23 consider breaking into a function and calling at the start of the app
#

# couriers = text_functions.read_data_from_csv("couriers.csv")
# #products = text_functions.read_data_from_csv("products.csv")
# orders = text_functions.read_data_from_csv("orders.csv")
products = db_functions.read_product_data_from_db()

print(products)

print("""
      
Welcome to the..
__________                   .___             __     _____                 
\______   \_______  ____   __| _/_ __   _____/  |_  /  _  \ ______ ______  
 |     ___/\_  __ \/  _ \ / __ |  |  \_/ ___\   __\/  /_\  \\____ \\____ \ 
 |    |     |  | \(  <_> ) /_/ |  |  /\  \___|  | /    |    \  |_> >  |_> >
 |____|     |__|   \____/\____ |____/  \___  >__| \____|__  /   __/|   __/ 
                              \/           \/             \/|__|   |__|    
""")


def RunApp():
    user_input_main = menu_functions.main_menu()
    while user_input_main != "0":
        
        if user_input_main == "1":
            user_input_product = menu_functions.product_menu()
            
            while user_input_product != 5:
                
                if user_input_product == "1":
                    print_functions.print_list(products)
                    
                elif user_input_product == "2":
                    new_product_name = input("What product would you like to add? (Press 0 to cancel!) ")
                    new_price = float(input("What is the price of this product?"))
                    new_product_index = max([int(product["index"])for product in products]) + 1 #
                    if new_product_name == "0":
                        menu_functions.product_menu()
                    
                    new_product = {                             # function adds a product to a table
                        "index": new_product_index, 
                        "name": new_product_name,
                        "price": new_price}
                    
                    update_functions.add_dict_to_list(new_product, products) #
                    save_functions.save_dict_products_to_csv("products.csv", products) #
                elif user_input_product == "3":
                    product_name = input("What product would you like to update? (Press 0 to cancel!)")
                    while True:
                        for product in products:
                            updated_product_name = input("Please enter the updated Product name")
                            if updated_product_name != "":
                                product['name'] = updated_product_name
                            updated_product_price = float(input("What is the updated price of this product?"))
                            if updated_product_price != "":
                                product['price'] = updated_product_price
                                break
                elif user_input_product == "4":
                    delete_product = input("What product would you like to delete? (Press 0 to cancel!)")
                    
                    for product in products:
                        
                        if product['name'] == delete_product:
                        
                            update_functions.delete_dict_in_list(product, products)
                            
                    if delete_product == "0":
                        menu_functions.product_menu()
                    
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
                    print_functions.print_list(couriers)
                    
                elif user_input_courier == "2":
                    new_courier_name = input("Which courier would you like to add? (Press 0 to cancel!)")
                    new_courier_phone = int(input("What is the contact number of the courier?"))
                    new_courier_index = max([int(courier["index"])for courier in couriers]) + 1
                    new_courier = {
                        "index": new_courier_index,
                        "name": new_courier_name,
                        "phone": new_courier_phone}
                    
                    update_functions.add_dict_to_list(new_courier, couriers)
                    save_functions.save_dict_couriers_to_csv("couriers.csv", couriers)
                    
                    if new_courier_name == "0":
                        menu_functions.courier_menu()
                    
                elif user_input_courier == "3":
                    courier_name = input("Which courier would you like to delete? (Press 0 to cancel!)")
                    
                    for courier in couriers:
                        
                        if courier['name'] == courier_name:
                            update_functions.delete_dict_in_list(courier, couriers)
                        if courier == "0":
                            menu_functions.courier_menu()
                    update_functions.delete_item_in_list(courier_name, couriers)
                    
                elif user_input_courier == "4":
                    courier_name = input("Which courier details would you like to update? (Press 0 to cancel!)")
                    
                    for courier in couriers:
                        
                        if courier['name'] == courier_name:
                            while True:
                                new_courier_name = input("Please enter the updated courier's name")
                                if new_courier_name != "":
                                    courier['name'] = new_courier_name
                                new_courier_phone = input("Please enter the updated phone number of the courier")
                                if new_courier_phone != "":
                                    courier['phone'] = new_courier_phone
                                    
                                break
                elif user_input_courier == "5":
                    break
                user_input_courier = menu_functions.courier_menu()
            user_input_main = menu_functions.main_menu()
        elif user_input_main == "3":
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
            #db_functions.close_connection()
            exit() # Close connection just before where you exit the app
            
        elif user_input_main == "0":
            menu_functions.main_menu() 
RunApp()

# Enter address as string (.split into objects)
# Refining functions
# print to a table (pip install pretty table)



