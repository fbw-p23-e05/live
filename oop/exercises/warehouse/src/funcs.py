######################################
# Helper functions - No need to
# modify this file
######################################
from factory_class import WorkerFactory
from worker import DeliveryMan, Packager
from warehouse import Warehouse


def add_employees():
    print("How many employees to add:")
    try:
        delivery = int(input("Indicate number of delivery men: "))
        packager = int(input("Indicate number of packagers: "))
        for i in range(delivery):
            WorkerFactory.create_object("delivery")
        for i in range(packager):
            WorkerFactory.create_object("packager")
    except ValueError:
        print("Invalid input")


def get_employees_numbers():
    delivery = 0
    packager = 0
    for employee in Warehouse().employee_list:
        if isinstance(employee, DeliveryMan):
            delivery += 1
        elif isinstance(employee, Packager):
            packager += 1
    return delivery, packager
