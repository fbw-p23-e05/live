"""A script that uses all modules from calculations package."""
from calculations.addition import addition
from calculations.ceiling import ceiling
from calculations.powering import power
from calculations.subtraction import subtraction

add_result = addition(45, 78)
print("The result of addition is:", add_result)

ceil_result = ceiling(39 / 4)
print("The result of ceiling is:", ceil_result)

power_result = power(25, 7)
print("The result of powering is:", power_result)

sub_result = subtraction(96, 38)
print("The result of subtraction is:", sub_result)
