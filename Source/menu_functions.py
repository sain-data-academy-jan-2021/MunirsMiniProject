from prettytable import from_db_cursor
import os

def main_menu():
    header()
    choice = input("""
1. Product Menu
2. Courier Menu
3. Order Menu
4. Save data and exit
0. Exit App """)
    return choice

def product_menu():
    product_menu_header()
    product_choice = input("""
1. Show Product list
2. Add Product
3. Update Product
4. Delete Product
5. Main Menu              """)
    return product_choice

def courier_menu():
    courier_menu_header()
    courier_choice = input("""
1. Show Courier List
2. Add Courier
3. Remove Courier
4. Update Courier
5. Main Menu     """)
    return courier_choice

def sub_menu(item, connection):
    option = input(f"Press 0 to return to {item} menu, or press 1 to exit app: ")
    if option == "0":
        os.system('clear')
        return
    elif option == "1":
        connection.close()
        exit()
    else:
        connection.close()
        exit()


def order_menu():
    order_menu_header()
    order_choice = input("""
1. Show Order list
2. Create New Order
3. Update Order Status
4. Update Order
5. Delete Order
6. Main Menu  """)
    return order_choice

def header():
    print(
"""
8888888b.                       888                   888           d8888                   
888   Y88b                      888                   888          d88888                   
888    888                      888                   888         d88P888                   
888   d88P 888d888 .d88b.   .d88888 888  888  .d8888b 888888     d88P 888 88888b.  88888b.  
8888888P"  888P"  d88""88b d88" 888 888  888 d88P"    888       d88P  888 888 "88b 888 "88b 
888        888    888  888 888  888 888  888 888      888      d88P   888 888  888 888  888 
888        888    Y88..88P Y88b 888 Y88b 888 Y88b.    Y88b.   d8888888888 888 d88P 888 d88P 
888        888     "Y88P"   "Y88888  "Y88888  "Y8888P  "Y888 d88P     888 88888P"  88888P"  
                                                                          888      888      
                                                                          888      888      
                                                                          888      888      

""")

def product_menu_header():
    print("""
8888888b.                       888                   888         888b     d888                            
888   Y88b                      888                   888         8888b   d8888                            
888    888                      888                   888         88888b.d88888                            
888   d88P 888d888 .d88b.   .d88888 888  888  .d8888b 888888      888Y88888P888  .d88b.  88888b.  888  888 
8888888P"  888P"  d88""88b d88" 888 888  888 d88P"    888         888 Y888P 888 d8P  Y8b 888 "88b 888  888 
888        888    888  888 888  888 888  888 888      888         888  Y8P  888 88888888 888  888 888  888 
888        888    Y88..88P Y88b 888 Y88b 888 Y88b.    Y88b.       888   "   888 Y8b.     888  888 Y88b 888 
888        888     "Y88P"   "Y88888  "Y88888  "Y8888P  "Y888      888       888  "Y8888  888  888  "Y88888 
                                                                                                           
                                                                                                           
                                                                                                           
""")

def courier_menu_header():
    print("""
 .d8888b.                            d8b                       888b     d888                            
d88P  Y88b                           Y8P                       8888b   d8888                            
888    888                                                     88888b.d88888                            
888         .d88b.  888  888 888d888 888  .d88b.  888d888      888Y88888P888  .d88b.  88888b.  888  888 
888        d88""88b 888  888 888P"   888 d8P  Y8b 888P"        888 Y888P 888 d8P  Y8b 888 "88b 888  888 
888    888 888  888 888  888 888     888 88888888 888          888  Y8P  888 88888888 888  888 888  888 
Y88b  d88P Y88..88P Y88b 888 888     888 Y8b.     888          888   "   888 Y8b.     888  888 Y88b 888 
 "Y8888P"   "Y88P"   "Y88888 888     888  "Y8888  888          888       888  "Y8888  888  888  "Y88888 
                                                                                                        
                                                                                                        
                                                                                                        
""")

def order_menu_header():
    print("""
 .d88888b.              888                       888b     d888                            
d88P" "Y88b             888                       8888b   d8888                            
888     888             888                       88888b.d88888                            
888     888 888d888 .d88888  .d88b.  888d888      888Y88888P888  .d88b.  88888b.  888  888 
888     888 888P"  d88" 888 d8P  Y8b 888P"        888 Y888P 888 d8P  Y8b 888 "88b 888  888 
888     888 888    888  888 88888888 888          888  Y8P  888 88888888 888  888 888  888 
Y88b. .d88P 888    Y88b 888 Y8b.     888          888   "   888 Y8b.     888  888 Y88b 888 
 "Y88888P"  888     "Y88888  "Y8888  888          888       888  "Y8888  888  888  "Y88888 
                                                                                           
                                                                                           
                                                                                           
""")

def main_menu_header():
    print("""
888b     d888          d8b               888b     d888                            
8888b   d8888          Y8P               8888b   d8888                            
88888b.d88888                            88888b.d88888                            
888Y88888P888  8888b.  888 88888b.       888Y88888P888  .d88b.  88888b.  888  888 
888 Y888P 888     "88b 888 888 "88b      888 Y888P 888 d8P  Y8b 888 "88b 888  888 
888  Y8P  888 .d888888 888 888  888      888  Y8P  888 88888888 888  888 888  888 
888   "   888 888  888 888 888  888      888   "   888 Y8b.     888  888 Y88b 888 
888       888 "Y888888 888 888  888      888       888  "Y8888  888  888  "Y88888 
                                                                                  
                                                                                  
                                                                                  
""")