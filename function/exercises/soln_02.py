
# Task 1

# def isOdd(num):
#     return bool(num % 2)

# def isEven(num):
#     return not bool(num % 2)

#     # if num % 2 == 0:
#     #     return False
#     # else:
#     #     return True


# print(isOdd(1), isEven(1))
# print(isOdd(657842), isEven(657842))
# print(isOdd(0), isEven(0))


# 50 % 2 = bool(200)
# Task 2


# def getParity(num, parity):
#     if parity == 'odd':
#         return bool(num % 2)
#     elif parity == 'even':
#         return not bool(num % 2)

# def getParity(num, parity):
#     if parity == 'odd':
#         return num % 2 != 0
#     elif parity == 'even':
#         return num % 2 == 0
#     else:
#         return 'Parity indicated is unknown'
    
# print(getParity(5, 'hfasfhfh97557#+#+'))
# print(getParity(-2, 'even'), getParity(101, 'even'))

# def getParity(num, num_type):
#     if num_type == 'odd':
#         if num % 2 == 0:
#             return False
#         else:
#             return True
#     if num_type == 'even':
#         if num % 2 == 0:
#             return True
#         else:
#             return False     
#     else:
#         return 'Number type indicated is unknown'
    
# print(getParity(20, 'The tale of two cities.'))

# print(not bool(0))

# not True = False

# Task 3

# import datetime as dt

# def greet(name, date):
#     if date.hour < 6:
#         print(f'Good Night, {name}!')
#     elif 6 < date.hour < 12:
#         print(f'Good Morning, {name}!')
#     else:
#         print(f'Good Afternoon, {name}!')

# greet('Alex', dt.datetime(2023, 9, 28, 6, 13, 25))

# greet('Alex', '2023-09-28 16:30:44')


# date = dt.datetime(2023, 9, 28, 4, 13, 25)

# print(type(date.hour))


# Task 4

# test1 = [[0, 2, 4, 5]]
# test2 = [
#     [0, 2, 4, 5],
#     [6],
#     [0, 2, 4, 5, 1, 4, 3, 2],
#     [4, 40]
# ]

# test3 = [[100, 200, 300], [700, 23]]

# test4 =[[]]

# def sumAll(*lists):
#     total = 0

#     for i in lists:
#         for j in i:
#             total += j

#     return total

# def sumAll(*lists):
#     total = 0

#     for i in lists:
#         total += sum(i)

#     return total

# def sumAll(*lists):
#     # total = 0

#     total = sum([sum(i) for i in lists])

#     return total
    

# print(sumAll(*test1, *test2, *test3, *test4))

# simple_list = [3, 5, 10]

# print(sum(simple_list))


# Task 5
song = ['Far across the distace and spaces between us']



def pig_latin(*texts, suffix='ay', single=False):

    e = []

    for text in texts:
        words = text.split(' ')

        for word in words:
            first_chr = word[0].lower()

            if first_chr in 'aeiou':
                vow_word = (word + suffix).capitalize()
                e.append(vow_word)
            else:
                con_word = (word[1:] + word[0] + suffix).capitalize()
                e.append(con_word)

    if single == True:
    
        emp = []

        for word in texts:
            first_chr = word[0].lower()

            if first_chr in 'aeiou':
                vow_word = (word + suffix).capitalize()
                emp.append(vow_word)
            else:
                con_word = (word[1:] + word[0] + suffix).capitalize()
                emp.append(con_word)
        s = ' '.join(emp)
        return s

    return e


test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}


print(pig_latin(*test2_data, **test2_config))













# print(pig_latin(*song, single=True))

# print(e)

    


