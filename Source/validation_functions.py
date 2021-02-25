import os

def getFloat(message):
    while True:
        try:
            userFloat = float(input(message))
            return userFloat
        except ValueError:
            print('You must enter a number in the format of x.xx')

def getInteger(message):
    while True:
        try:
            userInt = int(input(message))
            return userInt
        except ValueError:
            print('You must enter a number!')

def validity_checker(valid_options, option):
    while True:
        if option in valid_options:
            return option
        else:
            option = input("You have entered an invalid option, please try again: ")


