class CustomError(Exception):
    pass


class SomethingHappened(Exception):
    pass


class SalaryNotInRangeError(Exception):
    """
    Exception will be raised for errors regarding Salary.
    
    Attributes:
        message - error to display explaining error.
    """
    # Class attribute
    min_salary = 5000
    max_salary = 20000
    
    def __init__(self, salary, *args):
        super().__init__(args)
        self.salary = salary
        
    def __str__(self):
        return f"The {self.salary} is not in the recognized range of {self.min_salary, self.max_salary}"



