# Import pdb module
import pdb

# # Trigger debugger from this line
# pdb.set_trace()
num_list = [10, 35, 56, 76, 100, 340, 570, 890]
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter + str(number))
            

nested_loop()
    