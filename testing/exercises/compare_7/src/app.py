#!/usr/bin/env python
from typing import Union, Callable


def compare_to_seven(input: Union[int, str, Callable]) -> str:
    
    # TODO: write function

    if isinstance(input, int):
        number = input
    elif isinstance(input, str):
        if input.isnumeric():
            number = int(input)
        elif len(input) != 1:
            number = 0
        else:
            number = ord(input)
    else:
        number = 0

    
    if number > 7:
        return f'{input} is higher than 7.'
    elif number < 7:
        return f'{input} is lower than 7.'
    else:
        return f'{input} is 7.'
    


# print(type(compare_to_seven(compare_to_seven)))
        
    






if __name__ == "__main__":
    compare_to_seven(8)
