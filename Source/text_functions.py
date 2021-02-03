import csv

def Text2List(fileName):
        with open(fileName, "r") as fileholder:
            info = fileholder.read().splitlines()
            return(info)

def read_data_from_csv_orders():
    orders_list = []
    with open("orders.csv", "r") as orders_file:
        orders = csv.DictReader(orders_file)
        for line in orders:
            orders_list.append(line)
            return orders_list

def read_data_from_csv_products():
    products_list = []
    with open("products.csv", "r") as products_file:
        products = csv.DictReader(products_file)
        for line in products:
            products_list.append(line)
            return products_list

def read_data_from_csv_couriers():
    couriers_list = []
    with open("couriers.csv", "r") as couriers_file:
        couriers = csv.DictReader(couriers_file)
        for line in couriers:
            couriers_list.append(line)
            return couriers_list