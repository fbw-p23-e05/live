
# Task 1

# prompt_num = input('Input a number: ')

# num_int = int(prompt_num)

# print(f'Results of multiplication by {num_int}:')

# # for i in range(1, 10+1):
# #     print(f'{num_int} x {i} = {num_int * i}')

# table = (f'{num_int} x {i} = {num_int * i}' for i in range(1, 10+1))

# for i in table:
#     print(i)

# print(type(table))



# Task 2

# def pattern(num):
#     for i in range(1, num + 1):
#         print(str(i) * i)


# pattern(9)


# for i in range(1, 10):
#         print(str(i) * i)

# text = str(5)

# print(text * 10)



# Task 3
# 'starship'

# word = input('Input a word to reverse: ')


# reversed_word = word[::-1]
# print(reversed_word)

# e = ''

# for i in range(-1, -(len(word)+1), -1):
#     print(word[i], end='')

# for i in range(len(word)-1, -1, -1):
#     print(word[i], end='')


# for i in range(len(word)):
#     print(word[-i-1], end='')


# Task 4


# text = "Hello, I love you, won't you tell me your name?" 
# # print(text.replace('o', 'O'))

# e = ''

# try:
#     for i in text:
#         if i == 'o':
#             e += i.upper()
#         else:
#             e += i
# except:
#     print('Something went wrong.')

# finally:
#     print(e)


# Task 5


text = input('Input your characters: ')

count_digits = 0
count_letters = 0

try:
    for i in text:
        if i.isdigit():
            count_digits += 1
        elif i.isalpha():
            count_letters += 1
except:
    print('There is an emergency issue with the text.')

finally:
    print(f'Number of digits:  {count_digits}')
    print(f'Number of letters:  {count_letters}')




