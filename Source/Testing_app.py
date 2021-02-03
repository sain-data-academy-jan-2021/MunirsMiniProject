import sys
import print_functions
import save_functions
import update_functions 
import menu_functions
import text_functions
import csv

couriers = text_functions.read_data_from_csv_couriers()
products = text_functions.read_data_from_csv_products()
orders = text_functions.read_data_from_csv_orders()

# orders = [{
# "customer_name": "John",
# "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
# "customer_phone": "0789887334",
# "customer_courier": "2",
# "status": "preparing",
# "order": ""},

# {
# "customer_name": "Mike",
# "customer_address": "104 Canfield Road, LONDON, E1L 5TR",
# "customer_phone": "07800900834",
# "customer_courier": "5",
# "status": "preparing",
# "order": ""}]

# products = text_functions.Text2List("products.txt")
# couriers = text_functions.Text2List("couriers.txt")

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
                    if new_product_name == "0":
                        menu_functions.product_menu()
                    
                    new_product = {
                        "name": new_product_name,
                        "price": new_price}
                    
                    update_functions.add_dict_to_list(new_product, products)
                elif user_input_product == "3":
                    product_name = input("What product would you like to update? (Press 0 to cancel!)")
                    
                    for product in products:
                        while True:
                            updated_product_name = input("Please enter the updated Product name")
                            product['name'] = updated_product_name
                            if updated_product_name != "":
                                pass
                            
                            updated_product_price = float("What is the updated price of this product?")
                            product['price'] = updated_product_price
                            if updated_product_price != "":
                                pass
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
                    new_courier = input("Which courier would you like to add? (Press 0 to cancel!)")
                    
                    if new_courier == "0":
                        menu_functions.courier_menu()
                    update_functions.add_item_to_list(new_courier, couriers)
                    save_functions.save_lists("couriers.txt", couriers)
                    
                elif user_input_courier == "3":
                    delete_courier = input("Which courier would you like to delete? (Press 0 to cancel!)")
                    
                    if delete_courier == "0":
                        menu_functions.courier_menu()
                    update_functions.delete_item_in_list(delete_courier, couriers)
                    
                elif user_input_courier == "4":
                    update_courier = input("Which name would you like to update? (Press 0 to cancel!)")
                    
                    if update_courier == "0":
                        menu_functions.courier_menu()
                    updated_courier = input("What name you like to update this to? (Press 0 to cancel!)")
                    
                    if updated_courier == "0":
                        menu_functions.courier_menu()
                    update_functions.update_item_in_list(update_courier, updated_courier, couriers)
                    save_functions.save_lists("couriers.txt", couriers)
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
                    print(couriers)
                    new_order_courier = input("Please enter the courier you would like to deliver the order: ")
                    new_order = {
                        "customer_name": new_order_name,
                        "customer_phone": new_order_phone,
                        "customer_address": new_order_address,
                        "courier": new_order_courier,
                        "status": "Preparing"}
                        
                    update_functions.add_dict_to_list(new_order, orders)
                    save_functions.save_dict_to_csv("orders.csv", new_order)
                    
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
                                order['customer_phone'] = new_order_phone
                                if new_order_phone == " ":
                                    pass
                                new_order_address = input("Please enter the updated address of the customer: ")
                                order['customer_address'] = new_order_address
                                if new_order_address == " ":
                                    pass
                                print("The available couriers are::")
                                print(couriers)
                                new_order_courier = input("Please enter the courier you would like to deliver the order: ")
                                order['courier'] = new_order_courier
                                order['status'] = "Preparing"
                                if new_order_courier == " ":
                                    pass
                                break
                                # update_functions.add_dict_to_list(order, orders)
                            
                elif user_input_order == "5":
                    order_name = input("Whose order would you like to delete? ")
                    
                    for order in orders:
                        
                        if order['customer_name'] == order_name:
                            
                            update_functions.delete_dict_in_list(order, orders)
                            
                elif user_input_order == "6":
                    save_functions.save_dict_to_csv("orders.csv", orders)
                    break
                    menu_functions.main_menu()
                user_input_order = menu_functions.order_menu()
            user_input_main = menu_functions.main_menu()
                    
        elif user_input_main == "0":
            menu_functions.main_menu() 
RunApp()




