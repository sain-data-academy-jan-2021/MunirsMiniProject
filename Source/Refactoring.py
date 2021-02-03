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
                        
                        if product['name'] == delete_product
                        
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
            
            #------------------
            
            user_input_courier = menu_functions.courier_menu()
            
            while user_input_courier != 5:
                
                if user_input_courier == "1":
                    print_functions.print_list(couriers)
                    
                elif user_input_courier == "2":
                    new_courier_name = input("Which courier would you like to add? (Press 0 to cancel!)")
                    new_courier_phone = int(input("What is the contact number of the courier?"))
                    new_courier = {
                        "name": new_courier_name,
                        "phone": new_courier_phone}
                    
                    update_functions.add_dict_to_ist(new_courier, couriers)
                    
                    if new_courier_name == "0":
                        menu_functions.courier_menu()
                    
                elif user_input_courier == "3":
                    courier_name = input("Which courier would you like to delete? (Press 0 to cancel!)")
                    
                    for courier in couriers:
                        
                        if courier['name'] == courier_name
                        
                            update_functions.delete_dict_in_list(courier, couriers)
                    if delete_courier == "0":
                        menu_functions.courier_menu()
                    update_functions.delete_item_in_list(delete_courier, couriers)
                    
                elif user_input_courier == "4":
                    courier_name = input("Which courier details would you like to update? (Press 0 to cancel!)")
                    
                    for courier in couriers:
                        
                        if courier['name'] == courier_name
                            while True:
                                new_courier_name = input("Please enter the updated courier's name")
                                courier['name'] = new_courier_name
                                
                                if new_courier_name != "":
                                    pass
                                
                                new_courier_phone = input("Please enter the updated phone number of the courier")
                                courier['phone'] = new_courier_phone
                                
                                if new_courier_phone != "":
                                    pass
                                break
                    if update_courier == "0":
                        menu_functions.courier_menu()
                        
                    update_functions.update_item_in_list(update_courier, updated_courier, couriers)
                    save_functions.save_lists("couriers.txt", couriers)
                elif user_input_courier == "5":
                    break
                user_input_courier = menu_functions.courier_menu()
            user_input_main = menu_functions.main_menu()