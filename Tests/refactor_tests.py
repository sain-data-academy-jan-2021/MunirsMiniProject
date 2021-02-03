
# Example 12*4+7/4
# Example 2 - ignore errors person = create_person(firstname, surname, age, city, nationality, gender, height, weight)
# Example 3 def get_lengthy_condition(data): return data is not None and data != "" and len(data) > 3 and len(data) < 20

12 * 4 + 7 / 4

person = create_person(
                    firstname,
                    surname, 
                    age, 
                    city, 
                    nationality, 
                    gender, 
                    height, 
                    weight)


def get_condition_data(data):
    if data and len(data) > 3 and len(data) < 20:
        return True
    return False
