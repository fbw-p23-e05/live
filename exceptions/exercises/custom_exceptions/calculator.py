

# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):
  pass
#   def __init__(self, *args: object, notification='New information', tweet='Post a new tweet') -> None:
#     super().__init__(*args, notification, tweet)
#     print('It will be printed always.')

# write a function called parse_input that parses all the user input according to rules list defined in the exercise text
def parse_input(user_input):

    input_list = user_input.split()

    if len(input_list) != 3:
      raise MathematicalError('The input must consist of 3 elements')
    

    # try:
     
    #  if len(input_list) == 3:
    #   n1, op, n2 = input_list
    #  else:
    #    raise MathematicalError
     
    # except MathematicalError:
    #   print('The input must consist of 3 elements')

    #   raise MathematicalError('The input must consist of 3 elements')
    
    # n1 = input_list[0]
    # op = n1 = input_list[1]
    # n2 = input_list[2]
    
    n1, op, n2 = input_list

    try:
      n1 = float(n1)
      n2 = float(n2)

    except ValueError:
      raise MathematicalError('The conversion to float values is not possible.')
    
    # if op != '+' or op != '-' or op != '*' or op != '/':
    # if op not in '+-*/':
    if op not in ['+', '-', '*', '/']:
      raise MathematicalError('The second input must be an operator.')
    
    return n1, op, n2
    
# parse_input(user_input=input())

# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2

while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)



