import print_functions

def update_item_in_list(item_old, item_new, list):
    if item_old in list:
        list.remove(item_old)
        list.append(item_new)
        print_functions.print_list(list)

def add_item_to_list(item, list):
    list.append(item)
    print_functions.print_list(list)

def delete_item_in_list(item, list):
    if item in list:
        list.remove(item)
        print_functions.print_list(list)

def delete_dict_in_list(dict, list):
    if dict in list:
        list.remove(dict)

def add_dict_to_list(dict, list):
    list.append(dict)
    

def update_dict_in_list(dict_old, dict_new, list):
    if dict_old in list:
        list.remove(dict_old)
        list.append(dict_new)
        print_functions.print_list(list)
# def add_item_to_dict(key, value):
    