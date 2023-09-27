

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

print('Input few integers to calculate their average!\nInput 0 to exit!!!')

# n = True
total = 0
count = 0

try:
    while True:   
        num = int(input('Type an integer: '))
        if num != 0:
            total += num
            count += 1
        elif num == 0:
            avg = total / count
            print(avg)
            total = 0
            count = 0
            #False
except KeyboardInterrupt:
    print('Thanks for using the average calculator.')
except ZeroDivisionError:
    print('Thanks for using the average calculator. The count cannot be zero.')
except ValueError:
    print('Thanks for using the average calculator. Insert a number please.')
except:
    print('Review your code.')
    
    
   








