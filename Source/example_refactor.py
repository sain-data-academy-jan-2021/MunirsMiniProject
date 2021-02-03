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
                                order['customer_name'] = new_order_name
                                if new_order_name == " ":
                                    pass
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
                    