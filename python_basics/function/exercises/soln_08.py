
# Task 1

# add15 = lambda x: x + 15

# print(add15(100))
# print(add15(-2))

# Task 2

# isOdd = lambda x: x % 2 != 0

# isEven = lambda x: x % 2 == 0

# getParity = lambda x, parity: isOdd(x) if parity == 'odd' else isEven(x)

# print(isOdd(2), isEven(2))
# print(isOdd(1), isEven(1))
# print(getParity(2, 'odd'), getParity(2, 'even'))
# print(getParity(1, 'odd'), getParity(1, 'even'))

# Task 3

# starts_with_p = lambda s: s[0].lower() == 'p'

# starts_with_p = lambda s: s.lower().startswith('p')


# print(starts_with_p("Python"))
# print(starts_with_p("JavaScript"))
# print(starts_with_p("pirate"))



# Task 4

numbers = [2, 4, 5, 7, 9, 14]
factor = 2

multi_2 = lambda x: [(i * factor) for i in x]


print(multi_2(numbers))








