
# Task 1
import time
import sys

start_time = time.time()

def countdown(n):
    '''Prints a countdown starting from the given number.'''
    if n >= 0:
        print(n)
        countdown(n-1)

# countdown(5)

end_time = time.time()

print(end_time - start_time)

print(sys.getsizeof(countdown))

# 0.0000224113...
# Task 2

# def factorial(n):
#     '''Returns the factorial of a given number.'''
#     # if n == 0 or n == 1:
#     if n in (0, 1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# # print(factorial(5))
# print(factorial(0))
# print(factorial(1))
# print(factorial(10))


# Task 3

# def harmonic_sum(n):
#     '''Returns harmonic sum of the given positive integer number.'''
#     if n <= 0:
#         return 0
#     else:
#         return 1/n + harmonic_sum(n-1)

# print(harmonic_sum(7))
# print(harmonic_sum(4))
