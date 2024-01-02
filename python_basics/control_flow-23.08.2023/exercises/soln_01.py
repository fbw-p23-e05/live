# Task 1

# for i in range(3):
#     num = int(input('Enter number: '))

#     if num % 2 == 0:
#         print('Even number')
#     else:
#         print('Odd number')


# Task 2

# sum_num = 0

# for i in range(3):
#     num = int(input('Enter number: '))
#     sum_num += num

# print('Sum of the numbers: ', sum_num)

# Task 3


# max_num = None

# for i in range(5):
#     num = int(input('Enter number: '))
    
#     if max_num == None:
#         max_num = num
#     if num > max_num:
#         max_num = num

# print('Maximum of the numbers: ', max_num)
# max([4, -7, 40, 100, 20])

# max_num = 0
# e = []
# for i in range(5):
#     num = int(input('Enter number: '))
#     # e.append(num)
    
#     if num < max_num:
#         max_num = num
#     if num > max_num:
#         max_num = num

# print('Maximum of the numbers: ', max_num)


# Task 4

# num = int(input('Enter number: '))

# for i in range(2, num+1):
#     if num % i == 0:
#         print(i)


# Task 5

# num = int(input('Enter number: '))

# if num % 2 == 0 and num % 3 == 0:
#     print(num, 'is even and divisible by 3')
# elif num % 2 != 0 and num % 3 == 0:
#     print(num, 'is not even and divisible by 3')
# elif num % 2 != 0 and num % 3 != 0:
#     print(num, 'is not even and not divisible by 3')


# Task 6

num = int(input('Enter number: '))

if num >= 0 and num % 2 != 0 and num % 7 == 0:
    print(num, 'is positive, odd and divisible by 7')
elif num < 0 and num % 2 != 0 and num % 7 == 0:
    print(num, 'is negative, odd and divisible by 7')
elif num < 0 and num % 2 == 0 and num % 7 == 0:
    print(num, 'is negative, not odd and divisible by 7')
