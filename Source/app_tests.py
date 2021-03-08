from unittest.mock import patch, Mock
from update_functions import *
from print_functions import *
import os
from dotenv import load_dotenv
import pymysql


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


@patch('builtins.input')
@patch("validation_functions.getInteger")
@patch("update_functions.execute_sql_select")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_update_courier_in_db(mock_print, mock_execute, mock_execute_select, mock_validation, mock_input):
    mock_print.return_value = None
    mock_execute_select.return_value = [(22,), (24,), (26,)]
    mock_input.side_effect = ["Joan", "0123456789"]
    mock_validation.side_effect = [25,26,0]
    expected_SQL = (f'UPDATE couriers SET courier_name = "Joan", courier_phone = "0123456789" WHERE courier_id = "26"')
    expected_select_SQL = ('select courier_id from couriers')
    
    update_courier_in_db(None)

    mock_execute.assert_called_with(None, expected_SQL)
    mock_execute_select.assert_called_with(None, expected_select_SQL)



@patch("validation_functions.getInteger")
@patch("update_functions.execute_sql_select")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_delete_product_in_db(mock_print, mock_execute, mock_execute_select, mock_validation):
    mock_print.return_value = None
    mock_execute_select.return_value = [(22,), (24,), (26,)]
    mock_validation.side_effect = [25,26,0]
    expected_select_SQL = ('select product_id from products')
    expected_SQL = ('DELETE FROM products WHERE product_id = "26"')
    
    
    delete_product_in_db(None)
    
    
    mock_execute_select.assert_called_with(None, expected_select_SQL)
    mock_execute.assert_called_with(None, expected_SQL)


@patch("validation_functions.getInteger")
@patch("update_functions.execute_sql_select")
@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_courier_data_from_db")
def test_delete_courier_in_db(mock_print, mock_execute, mock_input, mock_execute_select, mock_validation):
    mock_print.return_value = None
    mock_execute_select.return_value = [(22,), (24,), (26,)]
    mock_validation.side_effect = [25,26,0]
    expected_select_SQL = ('select courier_id from couriers')
    expected_SQL = (f'DELETE FROM couriers WHERE courier_id = "26"')
    
    delete_courier_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)
    mock_execute_select.assert_called_with(None, expected_select_SQL)




@patch("validation_functions.getFloat")
@patch("validation_functions.getInteger")
@patch("update_functions.execute_sql_select")
@patch("builtins.input")
@patch("update_functions.execute_sql")
@patch("print_functions.read_product_data_from_db")
def test_update_product_in_db(mock_print, mock_execute, mock_input, mock_execute_select, mock_validation, mock_float_validation):
    mock_float_validation.side_effect = ["1.49"]
    mock_input.side_effect = ['Milk']
    mock_print.return_value = None
    mock_execute_select.return_value = [(22,), (24,), (26,)]
    mock_validation.side_effect = [21,26,0]
    expected_SQL = (f'UPDATE products SET product_name = "Milk", product_price = "1.49" WHERE product_id = "26"')
    expected_select_SQL = ('select product_id from products')
    
    update_product_in_db(None)
    
    mock_execute.assert_called_with(None, expected_SQL)
    mock_execute_select.assert_called_with(None, expected_select_SQL)

# @patch("builtins.input")
# @patch("update_functions.execute_sql")
# @patch("print_functions.read_courier_data_from_db")
# def test_add_courier_to_db(mock_print, mock_execute, mock_input):
#     mock_input.side_effect = ["Michelle", 123456789]
#     mock_print.return_value = None
#     expected_SQL = (f'INSERT INTO couriers (courier_name, courier_phone) VALUES ("Michelle", 123456789)')
    
#     add_courier_to_db(None)
    
#     mock_execute.assert_called_with(None, expected_SQL)


# @patch("validation_functions.getFloat")
# @patch("builtins.print")
# @patch("update_functions.execute_sql_select")
# @patch("builtins.input")
# @patch("update_functions.execute_sql")
# @patch("print_functions.read_product_data_from_db")
# def test_add_product_in_db(mock_print, mock_execute, mock_input, mock_execute_select, mock_builtin_print, mock_get_float):
#     mock_input.side_effect = ["Cheese","Bread"]
#     mock_get_float.return_value = 1.50
#     mock_print.return_value = None
#     mock_execute_select.return_value = ["Cheese"]
#     expected_select_SQL = ('select product_name from products')
#     expected_SQL = (f'INSERT INTO products (product_name, product_price) VALUES ("Bread", 1.50)')
    
#     add_product_in_db(None)
    
#     mock_builtin_print.assert_called_with("This product already exists, please try again!")
#     mock_execute.assert_called_with(None, expected_SQL)
#     #mock_execute_select.assert_called_with(None, expected_select_SQL)