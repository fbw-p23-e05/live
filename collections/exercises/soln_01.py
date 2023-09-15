
# Task 1

# fruits = []

# fruits.append('Apples')
# fruits.append('Cherries')
# fruits.append('Strawberries')

# for i in fruits:
#     print(i)


# Task 2

# cities = ['London', 'Paris', 'Berlin', 'Amsterdam']

# print('The capital city of Germany is:', cities[2])

# Task 3

# colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

# colors.remove('green')
# colors.remove('white')

# for i in colors:
#     print(i)

# Task 4

# letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']

# word = ''

# for i in letters:
#     word += i

# print(word.capitalize())


import re

# words = ['P', 'xPerth', 'London', 'Paris', 'Berlin', 'xPakistan', 'Amsterdam', 'xPen', 'Python']

# n = 0

# for i in words:
#     if re.match('P\w+', i):
#     # if re.search('^P\w+', i):
#     if i.startswith('P'):
#         n += 1

# print(n)
# if n >= 2:
#     print('There are 2 or more words starting with "P".')
# else:
#     print('There are not 2 or more words starting with "P".')



# "I’m a string"
# "I am the \”coolest\” string there is"
# "I just learned about ‘strings’ today"

# "I am "better" than anyone else because I end with a point."