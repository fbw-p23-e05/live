# import the sys module
import sys
import os

# Check if there are any arguments passed
# if len(sys.argv) > 1:
#     for arg in sys.argv:
#         print(arg)  
# else:
#     print("No arguments passed!")

# print("Usage: 'python3 sys-module.py <num1> <operator> <num2>")
# result = 0
# if len(sys.argv) == 4:
#     num1 = int(sys.argv[1])
#     operator = sys.argv[2]
#     num2 = int(sys.argv[3])
    
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             print("Cannot divide by zero")
#             sys.exit(1)
#         result = num1 / num2
        
#     else:
#         print("Invalid operator")
#         sys.exit(1)
        
# print(f"{num1} {operator} {num2} = {result}")

input_file = "newone.txt"

with open(input_file, "r") as file:
    sys.stdin = file
    for line in sys.stdin:
        print(line)

# standard output - sys.stdout

output_file = "output.txt"

with open(output_file, "w") as file:
    # Produces a file called output.txt
    sys.stdout = file
    
# error streams - sys.stderr

error_file = "errors.txt"

with open(error_file, "w") as file:
    list_1 = [1, 2, 3, 4]
    try:
        print(list_1[6])
    except IndexError as e:
        sys.stderr = file
        sys.stderr.write(str(e))
    