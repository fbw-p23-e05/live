# Task 1

# n = 0
# big_numbers = False

# while n < 3:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))

#     if num1 == num2:
#         print('Numbers are equal')
#     else:
#         print('Numbers are not equal')
    
#     if num1 > num2:
#         print('First number is greater than second number')
#     else:
#         print('Second number is greater than first number')

#     if num1 >= num2:
#         print('First number is greater than or equal to second number')
#     else:
#         print('Second number is greater than or equal to first number')

#     # if all(x>1000 for x in [num1, num2]):

#     if num1 > 1000 and num2 > 1000:
#         print('Both numbers are big!')
#         big_numbers = True
#     else:
#         print('Both numbers are not big!')
#         # big_numbers = False 
    
#     print('big_numbers is set to', big_numbers)
#     n += 1

# Task 2

print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')

month_name = input('Input the name of Month: ')

if month_name in ('January', 'March', 'May', 'July',' August', 'October', 'December'):
    print('Number of days: 31 days')
elif month_name in ('April', 'June', 'September', 'November'):
    print('Number of days: 30 days')
elif month_name == 'February':
    print('Number of days: 28 days')












