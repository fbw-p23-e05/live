import random

# guess = ''

guess = input('Guess the coin toss! Enter heads or tails: ')

# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     try:
#         guess = input()
#     except KeyboardInterrupt:
#         print('\nInsert again')

toss_dict = {0: 'tails', 1: 'heads'}

toss = toss_dict[random.randint(0, 1)] # 0 is tails, 1 is heads


if toss == guess: # 0 == 'tails'
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

