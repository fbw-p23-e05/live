from time import time as tt, ctime as ct

def singleton(cls):

    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    
    return get_instance

# Make this class a singleton
@singleton
class Warehouse:

    # instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls, *args, **kwargs)
    #     return cls.instance

    def __init__(self):
        self.num_employees = 0
        self.creation_time = ct(tt())
        self.employee_list = []

    def add_employee(self):
        self.num_employees += 1

    def __str__(self):
        return f"Warehouse created on {self.creation_time}. Employees: {self.num_employees}"
