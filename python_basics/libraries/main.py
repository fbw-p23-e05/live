import animal  # Importing the whole animal module

dog = animal.Animal()
dog.eat()
animal.create_name("Jack")


from person import Person, salary  # Import a specific part of the module

sarah = Person()
sarah.working()
print(salary)

# use '_' for spaces between module names
from dci_python import *  # Import all elements of the module

p23_e05 = P23E05()
p23_e05.current_mod()

print(class_manager)


import datetime as dt # Rename an import and use the new name 
from datetime import time as t

print(dt.datetime.now())
print(t.hour)

from customers.orders import *

order = Orders()
print(order)
