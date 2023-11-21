class Calculator:
    
    # Add
    def add(self, x, y):
        # Check if both variables are integers
        if not isinstance(x, int) or not isinstance(y, int):
            # Else: raise exception
            raise TypeError 
          
        # return the sum
        return x + y
    
    # Subtract
    def subtract(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x - y
        
        raise TypeError("Both values are supposed to be integers")
    
    # Multiply
    def multiply(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return x * y
        raise TypeError
    
    # Divide
    def divide(self, x, y):
        
        # Check if either of the values are not integers
        if not isinstance(x, int) or not isinstance(y, int):
            # raise TypeError
            raise TypeError("Both values must be integers.")
        
        # Check if y is equal to zero
        elif y == 0:
            # raise ZeroDivision Error
            raise ZeroDivisionError("You cannot divide by 0.")
        
        return x / y