from prettytable import from_db_cursor
import os

def main_menu():
    choice = input("""1. Product Menu
2. Courier Menu
3. Order Menu
4. Save data and exit
0. Exit App """)
    return choice

def product_menu():
    product_choice = input("""
1. Show Product list
2. Add Product
3. Update Product
4. Delete Product
5. Main Menu              """)
    return product_choice

def courier_menu():
    courier_choice = input("""
1. Show Courier List
2. Add Courier
3. Remove Courier
4. Update Courier
5. Main Menu     """)
    return courier_choice

def order_menu():
    order_choice = input("""
1. Show Order list
2. Create New Order
3. Update Order Status
4. Update Order
5. Delete Order
6. Main Menu  """)
    return order_choice

