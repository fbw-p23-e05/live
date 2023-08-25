

# Task 1

# num1 = int(input('First number: '))
# num2 = int(input('Second number: '))
# num3 = int(input('Third number: '))

# if num1 == num2 == num3:
#     sum_num = 3 * (num1 + num2 + num3)
# else:
#     sum_num = num1 + num2 + num3

# print('The sum is:', sum_num)


# Task 2

# num1 = int(input('First number: '))
# num2 = int(input('Second number: '))

# if num1 > num2:
#     result = 2 * (num1 - num2)
# else:
#     result = abs(num1 - num2)

# print('The result of calculation is', result)

# Task 3

# num = int(input('Number to check: '))

# if num % 2 == 0:
#     print(num, 'is an even number!')
# else:
#     print(num, 'is an odd number!')


# Task 4:

# import math
# r = float(input('Input the radius of the circle : '))

# area = round(math.pi * r**2, 2)

# print('The area of the circle with radius', r, 'is:', area)


# Task 5

# num = 7
# guess = int(input('Guess a number between 1 and 10 until you get it right : '))

# while guess != num:
#     guess = int(input('Guess a number between 1 and 10 until you get it right : '))

# print('Well guessed!')


# Task 6

# scale = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")

# temperature = int(input("Input the value of temperature you'd like to convert: "))

# if scale == 'C':
#     result = (temperature - 32) * 5/9
#     print('The temperature in Celsius is', result, 'degrees.')
# elif scale == 'F':
#     result = (temperature * 9/5) + 32
#     print('The temperature in Fahrenheit is', result, 'degrees.')
# else:
#     print('Please insert in right format.')


# Task 7

# print('* ', 2 * '* ', 3 * '* ', 4 * '* ', sep='\n')

# for i in range(5, 0, -1):
#     print(i * '* ')


# Task 8

num1 = 0
num2 = 1

while num1 <= 50:
    print(num1)
    #num1, num2 = num2, num1+num2
    num3 = num1 + num2
    num1 = num2  
    num2 = num3

    

