import sys
import print_functions
import save_functions
import update_functions 
import menu_functions
import text_functions
import validation_functions
import csv
import os
import pymysql
from prettytable import from_db_cursor

from dotenv import load_dotenv


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


connection = pymysql.connect(
  host,
  user,
  password,
  database
)

menu_functions.header()

def RunApp(connection):
    valid_options = ["1","2","3","4","0"]
    
    user_input_main = validation_functions.validity_checker(valid_options, menu_functions.main_menu())
    while user_input_main != "0":
        
        if user_input_main == "1":
            os.system('clear')
            menu_functions.product_menu_header()
            valid_options = ["1","2","3","4","5","0"]
            
            user_input_product = validation_functions.validity_checker(valid_options, menu_functions.product_menu())
            
            while user_input_product != 5:
                
                if user_input_product == "1":
                    os.system('clear')
                    
                    menu_functions.product_menu_header()
                    
                    print_functions.read_product_data_from_db(connection)
                    
                elif user_input_product == "2":
                    update_functions.add_product_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.product_menu_header()
                    
                elif user_input_product == "3":
                    update_functions.update_product_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.product_menu_header()
                    
                elif user_input_product == "4":
                    update_functions.delete_product_in_db(connection)
                    
                    os.system('clear')
                    
                    menu_functions.product_menu_header()
                    
                elif user_input_product == "5":
                    os.system('clear')
                    menu_functions.product_menu_header()
                    break
                    
                user_input_product = validation_functions.validity_checker(valid_options, menu_functions.product_menu())
                
            user_input_main = validation_functions.validity_checker(valid_options, menu_functions.main_menu())
            
        elif user_input_main == "2":
            os.system('clear')
            menu_functions.courier_menu_header()
            valid_options = ["1","2","3","4","5","0"]
            
            user_input_courier = validation_functions.validity_checker(valid_options, menu_functions.courier_menu())
            
            while user_input_courier != 5:
                
                if user_input_courier == "1":
                    os.system('clear')
                    menu_functions.courier_menu_header()
                    
                    print_functions.read_courier_data_from_db(connection)
                    
                elif user_input_courier == "2":
                    update_functions.add_courier_to_db(connection)
                    
                    os.system('clear')
                    menu_functions.courier_menu_header()
                    
                elif user_input_courier == "3":
                    update_functions.delete_courier_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.courier_menu_header()
                    
                elif user_input_courier == "4":
                    update_functions.update_courier_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.courier_menu_header()
                    
                elif user_input_courier == "5":
                    os.system('clear')
                    menu_functions.courier_menu_header()
                    break
                
                user_input_courier = validation_functions.validity_checker(valid_options, menu_functions.courier_menu())
                
            user_input_main = validation_functions.validity_checker(valid_options, menu_functions.main_menu())
            
        elif user_input_main == "3":
            os.system('clear')
            menu_functions.order_menu_header()
            valid_options = ["1","2","3","4","5","6","0"]
            
            user_input_order = validation_functions.validity_checker(valid_options, menu_functions.order_menu())
            
            while user_input_order != 6:
                
                if user_input_order == "1":
                    os.system('clear')
                    menu_functions.order_menu_header()
                    
                    print_functions.read_order_data_from_db(connection)
                    
                elif user_input_order == "2":
                    update_functions.add_order_to_db(connection)
                    
                    os.system('clear')
                    menu_functions.order_menu_header()
                    
                elif user_input_order == "3":
                    update_functions.update_order_status_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.order_menu_header()
                    
                elif user_input_order == "4":
                    update_functions.update_order_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.order_menu_header()
                    
                elif user_input_order == "5":
                    update_functions.delete_order_in_db(connection)
                    
                    os.system('clear')
                    menu_functions.order_menu_header()
                    
                elif user_input_order == "6":
                    os.system('clear')
                    menu_functions.order_menu_header()
                    break
                    
                    menu_functions.main_menu()
                    
                user_input_order = validation_functions.validity_checker(valid_options, menu_functions.order_menu())
                
            user_input_main = validation_functions.validity_checker(valid_options, menu_functions.main_menu())
            
        elif user_input_main == "4":
            os.system('clear')
            print("Your data has been saved, you will now exit the app")
            
            connection.close()
            
            exit()
            
        elif user_input_main == "0":
            print("You are now exiting the application, thankyou for using the ProductApp!")
            
            connection.close()
            
            exit()

RunApp(connection)


