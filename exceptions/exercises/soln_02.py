

# Task 1

# num = -5

# try:
#     while num <= 5:
#         if num != 0:
#             print(num, end=' ')
#         num += 1
# except:
#     print('The numbers are out of range.')


# Task 2

# import time

# lyrics = "Overhead the albatross Hangs motionless upon the air And deep beneath the rolling waves In labyrinths of coral caves"

# start = 0

# e = ''

# try:
#     while start < len(lyrics):
#         if lyrics[start].isupper():
#             e += lyrics[start].lower()
#         else:
#             e += lyrics[start].upper()
#         start += 1
#         print(lyrics[start])
#         time.sleep(2)
        
# except KeyboardInterrupt:
#     print('You forgot to close the while block.')

# finally:
#     print(e)


# Task 3

# print('Input few integers to calculate their average!\nInput 0 to exit!!!')

# # n = True
# total = 0
# count = 0

# try:
#     while True:   
#         num = int(input('Type an integer: '))
#         if num != 0:
#             total += num
#             count += 1
#         elif num == 0:
#             avg = total / count
#             print('Average of the above numbers is: ', avg)
#             total = 0
#             count = 0
#             #False
# except KeyboardInterrupt:
#     print('Thanks for using the average calculator.')
# except ZeroDivisionError:
#     print('Thanks for using the average calculator. The count cannot be zero.')
# except ValueError:
#     print('Thanks for using the average calculator. Insert a number please.')
# except:
#     print('Review your code.')


# Task 4
    
    
# text = "She came to me one morning One lonely Sunday morning Her long hair flowing in the mid-winter wind I know not how she found me For in darkness I was walking And destruction lay around me from a fight I could not win"

# print('Text:\n', text)

# to_find = input('What should be found?: ')

# indx = 0

# while indx < len(text):
#     if to_find == text[indx]:
#         print(f'Character {to_find} found at index {indx}')
#     indx += 1
    

# while indx < len(text):

#     position = text.find(to_find, indx)

#     if indx == position:   
#         print(f'Character {to_find} found at index {position}')
#     indx += 1


# Task 5
n = True

# while True:
while n:
    a = int(input('Type starting integer: '))
    b = int(input('Type ending integer: '))
    c = int(input('Type divisor: '))

    while a <= b and c != 0:
        if a % c == 0:
            print(f'{a}  is divisible by {c}')
        a += 1

    # break
    n = False






