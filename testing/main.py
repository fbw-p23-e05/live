import os 
from random import randint


def delete_file(filename):
    if os.remove(filename):
        return True
    else:
        return False


def new_func():
    print("This a new function")
    

def random_func():
    return randint(5, 10)
