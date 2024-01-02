# Task 2

# def fizzbuzz(maximum_value):
#     breakpoint()
#     for n in range(maximum_value):
#         if n % 5 == 0 and n % 3 == 0:
#             print('FizzBuzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         elif n % 5 == 0:
#             print('Buzz')        
#         else:
#             print(n)

# fizzbuzz(30)


# Task 3


# 0, 1, 1, 2, 3, 5, 8,.....34


# This function returns values quite fast O(n) time or O(n) space, it also has an error

def get_n(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_n(n - 1, memoize) + get_n(n-2, memoize)
        print(memoize)
        return memoize[n]

print(get_n(10))


# get_n(9, memoize) + get_n(8, memoize) # 34

# get_n(8, memoize) + get_n(7, memoize)

# get_n(7, memoize) + get_n(6, memoize) # 8 + 5

# get_n(6, memoize) + get_n(5, memoize)# 5 + 3

# get_n(5, memoize) + get_n(4, memoize) # 3 + 2

# 1 + 1

# 1 + 1

# get_n(2, memoize) + get_n(1, memoize)

# 1 + 0

# get_n(1, memoize) + get_n(0, memoize)