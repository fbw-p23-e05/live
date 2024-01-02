def add(x, y):
    """Adds 2 numbers and returns the sum."""
    return x + y


def subtract(x, y):
    """Subtracts y from x and returns the difference."""
    return x - y 


def multiply(x, y):
    """Multiples 2 numbers and returns the product."""
    return x * y


def divide(x, y):
    """Divides x by y and returns the quotient."""
    try: 
        result = x // y
        return result
    except ZeroDivisionError:
        print("Cannot not divide by zero.")
    
