from unittest.mock import patch, Mock
# import unittest
from update_functions import *
from print_functions import *

# class TestApp(unittest.TestCase):
    
@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_update_courier_in_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ['10', 'Joan', '0123456789']
    mock_print.return_value = None
    expected_SQL = (f'UPDATE couriers SET courier_name = "Joan", courier_phone = "0123456789" WHERE courier_id = "10"') 

    #Act
    update_courier_in_db(None)

    #Assert
    mock_execute.assert_called_with(None, expected_SQL)


@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_delete_product_in_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ['10', 'Cheese', 1.79]
    mock_print.return_value = None
    expected_SQL = (f'DELETE FROM products WHERE product_id = "10"')

    #Act
    delete_product_in_db(None)
    
    #Assert
    mock_execute.assert_called_with(None, expected_SQL)


@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_add_product_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ['Headphones', 20.12]
    mock_print.return_value = None
    expected_SQL = (f'INSERT INTO products (product_name, product_price) VALUES ("Headphones", 20.12)')
    
    add_product_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)
    

@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_update_product_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ['15', 'Milk', 1.49]
    mock_print.return_value = None
    expected_SQL = (f'UPDATE products SET product_name = "Milk", product_price = "1.49" WHERE product_id = "15"')
    
    update_product_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)


@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_add_courier_to_db(mock_print, mock_execute, mock_input):
    #Assemble
    mock_input.side_effect = ["Michelle", 123456789]
    mock_print.return_value = None
    expected_SQL = (f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("Michelle", 123456789)')
    #Act
    add_courier_to_db(None)
    #Assert
    mock_execute.assert_called_with(None, expected_SQL)


@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_delete_courier_in_db(mock_print, mock_execute, mock_input):
    mock_input.side_effect = ["1", "Lucy", 123456789]
    mock_print.return_value = None
    expected_SQL = (f'DELETE FROM couriers WHERE courier_id = "1"')
    
    delete_courier_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)


# if __name__ == '__main__':
#     unittest.main()