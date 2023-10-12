"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
import username, pick_chce, ........, ......
from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name

def get_username():  
    username = input('What is your user name?: ')
    return username


def decorator(func):
    def inner(*args, **kwargs):
        print('*' * 50)
        func(*args, **kwargs)
        print('*' * 50)

@decorator
def greet_user():
    print('Hello', get_username())


def show_menu():
    print(f'1. List items by warehouse, \n2. Search an item and place an order and \n3. Quit')


def pick_choice():
    choice = int(input('Enter your choice: '))
    return choice


def pick_1():
    print('Items in warehouse 1:')
    for i in warehouse1:
        print(i)
    for i in warehouse2:
        print('Items in warehouse 2:')
        print(i)


def pick_2():
    item = input('Enter a product name: ')
    # count_1 = 0
    # count_2 = 0
    if item in warehouse1:
        count_1 = warehouse1.count(item)
    if item in warehouse2:
        count_2 = warehouse2.count(item)

    for i in warehouse1:
        if i == item:
            count_1 += 1
    
    for i in warehouse2:
        if i == item:
            count_2 += 1

    if count_1 > count_2:
        .....

    print(f'Warehouse 1 has {count_1} of {item}')
    ....

    ....


def pick_3():
    print('Thank you for the visit.')



# Greet the user
username.get_username()
# Show the menu and ask to pick a choice
pick_chce.pick_choice()
# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
# query.py
def main():
    username.get_username()
    greet_user()
    show_menu(pick_1())
    pick_chce.pick_choice()
    
    pick_2()
    pick_3()


# main()

if __name__ == '__main__':
    main()
    




