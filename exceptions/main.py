# import the exception(s)
from exceptions import SomethingHappened, CustomError, SalaryNotInRangeError

list_1 = [1, 2, 3, 4, 5, 6, 7]

# try:
#     for num in range(len(list_1) + 2):
#         if num > len(list_1):
#             raise IndexError
#         print(num)
# except TypeError:
#     print("Hey, there's something wrong!")
# except KeyboardInterrupt:
#     print("The program has been interrupted")
# else:
#     print(list_1)
# finally:
#     print("I will always be executed.")
    
# dict_1 = {1: "One", 2: "Two", 3: "Three", 4: "Four"}

# try:
#     if "Five" not in dict_1.values():
#         raise TypeError
# except TypeError:
#     print(dict_1.values())

number = 28

# try:
#     input_num = int(input("Enter a number:"))
#     if input_num < number:
#         raise SomethingHappened
#     elif input_num > number:
#         raise CustomError
#     elif input_num == number:
#         print("You guessed correctly")
# except SomethingHappened: 
#     print("Oops, try guessing again.")
# except CustomError:
#     print("You probably guessed wrong!")

salary = int(input("What is your desired salary?: "))

try:
    if salary < SalaryNotInRangeError.min_salary or salary > SalaryNotInRangeError.max_salary:
        raise SalaryNotInRangeError(salary, 3000)
    else:
        print("Congratulations! You start on Monday.")
        
except SalaryNotInRangeError:
    print("Unfortunately we cannot meet your salary requirements")

    
