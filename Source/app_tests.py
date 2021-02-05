from update_functions import add_dict_to_list
from update_functions import update_dict_in_list
from text_functions import read_data_from_csv
from save_functions import save_dict_to_csv



def test_add_dict_to_list():
#Assemble
    test_list = [{"Mike":"07892848858"},{"Munir":"078395479"},]
    new_dict = {"Luke":"099349353"}
# #Act
    add_dict_to_list(new_dict,test_list)
#Assert
    assert len(test_list) == 3
    assert new_dict in test_list
    print("You've added a dictionary to a list successfully")

test_add_dict_to_list()


def test_read_data_from_csv_orders():
    #Assemble
    filename = "Source/test/couriers.csv"
    #Act
    new_data = read_data_from_csv(filename)
    #Assert
    assert len(new_data) == 1
    print("Data has been read from the CSV successfully")
    assert new_data[0]['name'] == "Mike"

test_read_data_from_csv_orders()



def test_save_dict_to_csv():
    #Assemble
    test_dict = [{"customer_name":"Munir","customer_address" : "", "customer_phone": "", "courier" : "","status":"", "items":""}]
    new_file = "Source/test/testwriting.csv"
    #Act
    save_dict_to_csv(new_file, test_dict)
    #Assert
    list_of_dicts = read_data_from_csv(new_file)
    assert len(list_of_dicts) == 1
    assert list_of_dicts[0]["customer_name"] == "Munir"
    print("This has worked")

test_save_dict_to_csv()