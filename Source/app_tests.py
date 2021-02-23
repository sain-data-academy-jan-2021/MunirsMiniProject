from update_functions import add_dict_to_list
from update_functions import update_dict_in_list
from text_functions import read_data_from_csv
from save_functions import save_dict_to_csv
from unittest.mock import patch, Mock
import update_functions

# def test_add_dict_to_list():
# #Assemble
#     test_list = [{"Mike":"07892848858"},{"Munir":"078395479"},]
#     new_dict = {"Luke":"099349353"}
# # #Act
#     add_dict_to_list(new_dict,test_list)
# #Assert
#     assert len(test_list) == 3
#     assert new_dict in test_list
#     print("You've added a dictionary to a list successfully")

# test_add_dict_to_list()


# def test_read_data_from_csv_orders():
#     #Assemble
#     filename = "Source/test/couriers.csv"
#     #Act
#     new_data = read_data_from_csv(filename)
#     #Assert
#     assert len(new_data) == 1
#     print("Data has been read from the CSV successfully")
#     assert new_data[0]['name'] == "Mike"

# test_read_data_from_csv_orders()



# def test_save_dict_to_csv():
#     #Assemble
#     test_dict = [{"customer_name":"Munir","customer_address" : "", "customer_phone": "", "courier" : "","status":"", "items":""}]
#     new_file = "Source/test/testwriting.csv"
#     #Act
#     save_dict_to_csv(new_file, test_dict)
#     #Assert
#     list_of_dicts = read_data_from_csv(new_file)
#     assert len(list_of_dicts) == 1
#     assert list_of_dicts[0]["customer_name"] == "Munir"
#     print("This has worked")

# Database Tests ----------------------------------------------------------------------------------------------------------

# Mocks print_functions, input x 3, execute_sql
@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_update_courier_in_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ['10', 'Joan', '0123456789']
    mock_print.return_value = None
    expected_SQL = (f'UPDATE couriers SET courier_name = "Joan", courier_phone = "0123456789" WHERE courier_id = "10"') 

    #Act
    update_functions.update_courier_in_db(None)

    #Assert
    mock_execute.assert_called_with(None, expected_SQL)

    print("This has worked")

test_update_courier_in_db()

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_delete_product_in_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ['10', 'Cheese', 1.79]
    mock_print.return_value = None
    expected_SQL = (f'DELETE FROM products WHERE product_id = "10"')

    #Act
    update_functions.delete_product_in_db(None)
    
    #Assert
    mock_execute.assert_called_with(None, expected_SQL)
    
    print("This has worked")

test_delete_product_in_db()

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_add_product_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ['Headphones', 20.12]
    mock_print.return_value = None
    expected_SQL = (f'INSERT INTO products (product_name, product_price) VALUES ("Headphones", 20.12)')
    
    update_functions.add_product_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)
    
    print("This has worked")

test_add_product_in_db()

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_update_product_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ['15', 'Milk', 1.49]
    mock_print.return_value = None
    expected_SQL = (f'UPDATE products SET product_name = "Milk", product_price = "1.49" WHERE product_id = "15"')
    
    update_functions.update_product_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)
    
    print("This has worked")
    

test_update_product_in_db()

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_add_courier_to_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ["Michelle", 123456789]
    mock_print.return_value = None
    expected_SQL = (f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("Michelle", 123456789)')

    #Act
    update_functions.add_courier_to_db(None)

    #Assert
    mock_execute.assert_called_with(None, expected_SQL)

    print("This has worked")

test_add_courier_to_db()

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_delete_courier_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ["1", "Lucy", 123456789]
    mock_print.return_value = None
    expected_SQL = (f'DELETE FROM couriers WHERE courier_id = "1"')
    
    update_functions.delete_courier_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)

    print("This has worked")

test_delete_courier_in_db()
