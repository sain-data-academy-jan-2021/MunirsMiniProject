import csv

def save_lists(fileName, list):
    with open(fileName, 'w') as list_file:
        list_file.writelines("%s\n" % line for line in list)

# def save_dict_to_csv(fileName, list):
#     with open(fileName, 'w') as dict_file:
#         field_names = ['customer_name','customer_address','customer_phone','courier','status']
#         writer = csv.DictWriter(dict_file, fieldnames=field_names)
#         writer.writeheader()
#         for order in list:
#             writer.writerow(order)

def save_dict_to_csv(fileName, dict):
    with open(fileName, 'w') as dict_file:
        field_names = ['customer_name','customer_address','customer_phone','courier','status']
        writer = csv.DictWriter(dict_file, fieldnames=field_names)
        writer.writeheader()
        for order in dict:
            writer.writerow(order)