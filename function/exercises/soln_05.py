
# Task 1

def validate_numeric(func):
    '''Validates if the input arguments of a function are numeric.'''
    def inner(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)): # and not isinstance(i, float):
                return 'The input arguments must be numeric'
        for kwarg in kwargs.values():
            if not isinstance(kwarg, (int, float)): # and not isinstance(i, float):
                return 'The input arguments must be numeric'
        return func(*args, **kwargs)

    return inner

# @validate_numeric
# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b

# print(sum(1, 2))
# print(sum(1, "2"))
# print(sum(a=1, b="a"))
# print(sum(a=1, b=3.4))


# Task 2

def debug(func):
    '''Outputs information about the input and output arguments.'''
    def inner(*args, **kwargs):
        print('*' * 10)

        if args:
            e_joined = ','.join([str(arg) for arg in args])

            # e = []
            # for i in args:
            #     e.append(str(i))
            # e_joined = ','.join(e)
            print(f'Positional arguments: {e_joined}')
        else:
            print('There are no positional arguments')

        if kwargs:
            e_joined = ','.join([f'{key}={value}' for key, value in kwargs.items()])

            # e = []
            # for key, value in kwargs.items():
            #     e.append(f'{key}={value}')
            # e_joined = ','.join(e)
            print(f'Keyword arguments: {e_joined}')
        else:
            print('There are no Keyword arguments')
        
        result = f'Result: {func(*args, **kwargs)}'
        print(result)
        return result
    
    return inner

@debug
@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

sum(1, 2)
sum(a=1, b=2)
sum(1, "a")
