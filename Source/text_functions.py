import csv

def Text2List(fileName):
        with open(fileName, "r") as fileholder:
            info = fileholder.read().splitlines()
        return(info)

def read_data_from_csv(filename):
    list = []
    with open(filename, 'r') as file:
        items = csv.DictReader(file)
        for line in items:
            list.append(line)
        return list


def courier_list_select():
    courierlist = read_data_from_csv("couriers.csv")
    cnum = []
    cname = []
    for courier in courierlist:
        cnum.append(courier['index'])
        cname.append(courier['name'])
    for i in range(len(cnum)):
        print(cnum[i] + '\t ' + cname[i])
    num = input("Please enter the number of the courier you would like to deliver the order: ")
    new_courier = courierlist[int(num) - 1]
    return new_courier


def product_list_select():
    productlist = read_data_from_csv("products.csv")
    pnum = []
    pname = []
    for product in productlist:
        pnum.append(product['index'])
        pname.append(product['name'])
    for i in range(len(pnum)):
        print(pnum[i] + '\t ' + pname[i])
    num = input("Please enter the number of the product you would like to add to the order: ")
    new_product = productlist[int(num) - 1]
    return new_product



