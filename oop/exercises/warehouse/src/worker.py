############################
# Do not modify this file
############################
from abc import ABC, abstractmethod
from warehouse import Warehouse


class Worker(ABC):
    def __init__(self):
        w = Warehouse()
        w.add_employee()
        w.employee_list.append(self)

    @abstractmethod
    def work(self):
        raise NotImplementedError("Abstract Method not Implemented")


class DeliveryMan(Worker):
    def work(self):
        print("Delivering packages to clients")


class Packager(Worker):
    def work(self):
        print("Placing products in packages")
