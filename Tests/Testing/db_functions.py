import pymysql
import os
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

# function to close connection
# function name - does it need any paramaters
# inside function - close the connection
# return what????
def close_connection():
    connection.close()

# def Text2List(fileName):
#         with open(fileName, "r") as fileholder:
#             info = fileholder.read().splitlines()
#         return(info)



def read_product_data_from_db():
    list = []
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products;')
    product_rows = cursor.fetchall()
    for row in product_rows:
        # create dictionary product
        product = {"id":row['id'],"name":row['name'],"price":row['price']}
        list.append(product)
    cursor.close()
        # append to list
    return list

def read_courier_data_from_db():
    list = []
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM couriers;')
    courier_rows = cursor.fetchall()
    for row in courier_rows:
        # create dictionary product
        courier = {"id":row['id'],"name":row['name'],"phone":row['phone']}
        list.append(courier)
    cursor.close()
        # append to list
    return list

# def print_data_from_db(database):
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM database;')
#     rows = cursor.fetchall()
#     for row in rows:
#         print row[1]
#     cursor.close()

# def update_date_in_db(database):
#     cursor = connection.cursor()
#     cursor.execute('UPDATE * FROM database;')

# def add_data_to_products_db():
#     cursor = connection.cursor()
#     sql_commands = 'INSERT INTO products (product_name, product_price) VALUES
#     cursor.execute(sql_commands)
    

# sql = "UPDATE customers SET product_name = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")
# # row = [ 'id', 'name', 'price']
# row = [id = 1, name = 'Milk', price ='2.99']
# row = [id = 2, name = 'Milky', price = '1.99']
# row = [3, 'Milka', '3.99']
# row = [4, 'Milks', '4.99']
# #id of the product = row[0] or row['id']
# #id of the product = row[0]

#         product = {"id":row[0],"name":row[1],"price":row[2]}

        
        

# rows = cursor.fetchall()
# for row in rows:
#   print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')



# def courier_list_select():
#     courierlist = read_data_from_csv("couriers.csv")
#     cnum = []
#     cname = []
#     for courier in courierlist:
#         cnum.append(courier['index'])
#         cname.append(courier['name'])
#     for i in range(len(cnum)):
#         print(cnum[i] + '\t ' + cname[i])
#     num = input("Please enter the number of the courier you would like to deliver the order: ")
#     new_courier = courierlist[int(num) - 1]
#     return new_courier


# def product_list_select():
#     productlist = read_data_from_csv("products.csv")
#     pnum = []
#     pname = []
#     for product in productlist:
#         pnum.append(product['index'])
#         pname.append(product['name'])
#     for i in range(len(pnum)):
#         print(pnum[i] + '\t ' + pname[i])
#     num = input("Please enter the number of the product you would like to add to the order: ")
#     new_product = productlist[int(num) - 1]
#     return new_product



