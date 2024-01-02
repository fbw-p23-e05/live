### Selection Control Flow

"""
if - helps us to run a particular piece of code, 
but only when a certain condition is true.
This statement only checks for one condition.
"""

a = 4

if a > 5:
    print('a is greater than 5')
    
    
"""
if-else - evaluates a condition and will execute the body if the test condition is true,
but if the condition false then the body of else is executed.
"""

# b = 5

# if b < 7:
#     print('b is less than 7')
# else:
#     print('b is more than 7')
    
    
"""
nested if - these are if statements inside of other if statements.
"""

# c = 3
# d = 5
# e = 15

# if c > d:
#     if c < e:
#         print('This value is in the middle')
#     else:
#         print('This is the biggest value.')
# else:
#     print('this is the smallest value.')


"""
if-elif-else - is used to conditionally execute a statement or block of code.
"""    

# x = 3
# y = 25

# if x == y:
#     print('x and y are equal.')
# elif x > y:
#     print('x is greater than y')
# # elif x < y:
# #     print('x is less than y.')
# else:
#     print('x is less than y.')
    

"""
and - all conditions have to be met in order to execute a statement or block of code.
"""

# balance = 500
# fees = 2
# min_withdrawal = 5

# if 3 + fees < balance and 3 > min_withdrawal:
#     print('You can withdraw your funds.')
    
    
"""
or - if either one of the conditions returns True then the code will be executed.
"""

# mileage = 15000
# year = 2017
# cc = 2000

# if mileage < 10000 or year >= 2017 and cc < 2500:
#     print('Hey, I would love to buy this car!')
    
    
"""
not - executes code if False or empty
"""

colour = 'Red'
used = True
accident_damaged = False


if not (used and accident_damaged):
    print('this is a new car')
else:
    print('This is a used car')
    
