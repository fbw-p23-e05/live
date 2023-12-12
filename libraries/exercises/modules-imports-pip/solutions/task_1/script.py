import math_mod
from string_mod import concat, create_string, check_digit

print("Result of adding 20 and 30 is", math_mod.add(20, 30))
print("Result of subtracting 40 and 20 is", math_mod.subtract(40, 20))
print("Result of multiplying 25 and 7 is", math_mod.multiply(25, 7))
print("Result of dividing 44 and 8 is", math_mod.divide(44, 8))

str_1 = "Hello"
str_2 = "DCI"

list_1 = ["My", "cat", "jumps", "over", "walls"]

str_3 = "PythonRocks2000"

print(f"Result of concatenation of {str_1} and {str_2} is {concat(str_1, str_2)}")
print("Result of creating a string a list is", create_string(list_1))
print(f"Result of checking digits in the string {str_3} is {check_digit(str_3)}")
