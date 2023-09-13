# Task 1

# def sum_nums(num1, num2):

#     # result = num1 + num2

#     return num1 + num2

# num1_inp = int(input('Enter number 1: '))
# num2_inp = int(input('Enter number 2: '))

# print(sum_nums(num1_inp, num2_inp))


# Task 2

# def check_even_odd(num):
#     if num % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# print(check_even_odd(10))


# Task 3


# def calculate_product(num1, num2 = 3):

#     return num1 * num2

# print(calculate_product(100))


# Task 4

# def all_nums(num):
#     # num = int(input('Enter a number: '))
#     for i in range(1, num+1):
#         print(i)

# all_nums(7)


# Task 5

# def all_nums(num):
#     n = 1
#     while n <= num:
#         print(n)
#         n += 1

# all_nums(10)


# Task 6

# def text_reverse(text):

#     # for i in text:
#     #     print(i)
    
#     # new_text = text[-1:-16:-1]

#     new_text = text[::-1]

#     # return new_text

# print(text_reverse('The last of us.'))


# Task 7

# def check_alphabets(text):

#     if text.isalpha():
#         return 'It contains only alphabetic characters.'
#     else:
#         return 'It does not contain only alphabetic characters.'
    
# print(check_alphabets('Thelastofus'))


# Task 8

# def num_sign(num):

#     if num < 0:
#         return 'Negative'
#     elif num > 0:
#         return 'Positive'
#     else:
#         return 'Zero'
     
# print(num_sign(0))


# Task 9

# import re

# def check_email(email):

#     check = re.match('^[\w.-]{1,24}@[\w]+\.[a-z]{2,3}$', email)

#     if check:
#         return "it's a valid email address"
#     else:
#         return "it's not a valid email address"
    
# print(check_email('life.is_short-on_planet@earth.de'))


# Task 10

# def calculate_statistics(n1, n2, n3, n4, n5):

#     max_num = max(n1, n2, n3, n4, n5)

#     min_num = min(n1, n2, n3, n4, n5)

#     avg_num = (n1 + n2 + n3 + n4 + n5) / 5

#     return f'Maximum number: {max_num}, Minimum number: {min_num}, Average of numbers: {avg_num}'

# print(calculate_statistics(4, -100, 20, 0, 44.23))


# Task 11

# a = 300

# def any_func():
#     global a
#     a = 5
#     return 10

# print(any_func())
# print(a)

# Task 12

def square(num):
    return num ** 2

def double(num):
    return num * 2


def combined_func(num):
    return double(square(num))

    # return square(num) + double(num)

print(square(4))
print(double(4))
print(combined_func(4))





