print("Welcome to the stone game!")

# Ask user to input total number of stones in the pile.
stone_pile = int(input('Enter the total number of stones in the pile: '))

# Ask the user to input maximum number of stones to be removed at each turn.
max_stone = int(input('Enter the maximum number of stones that can be taken at once: '))


# Prompt users to input their names.
player_1 = input('Enter name of Player 1: ')
player_2 = input('Enter name of Player 2: ')

# Ask the user to input the player number who will start the game.
who_start = int(input('Who should start the game? (1 for Player 1, 2 for Player 2): '))

print("Game Start!\n")

# Loop that continues as long as there are stones in the pile.
while stone_pile > 0:
    
    # Print the number of stones in the pile
    print("The current count is", stone_pile)
    
    # print("Hi", player_1, "and", player_2, "your stone count is", stone_pile)
    
    # print(f"Hi {player_1} and {player_2}, your stone count is {stone_pile}")
    
    # player_name = p1 if who_start == 1 else p2
    # taken_stones = int(
    #     input(
    #     f"{player_name}, how many stones will you take (1 to {min(max_stone, stone_pile)})"
    #     )
    # )
    
    current_player = ''
    
    # Checking who the first player is supposed to be
    if who_start == 1:
        # assign the player name to current_player
        current_player = player_1
    elif who_start == 2:
        current_player = player_2
        
    taken_stones = int(input(f'{current_player}, how many stones would you like to take? (between 1 and {max_stone})'))
    
    if taken_stones < 1 or taken_stones > stone_pile or taken_stones > max_stone:
        print("Invalid number, try again!")
        continue
    else:
        stone_pile -= taken_stones
    
    # who_start = 1 if who_start == 2 else 2
    
    # current_player = player_1 if current_player == player_1 else player_2
    
    # Check which player just had their turn
    if current_player == player_1:
        # Switch the value of who_start to opposite player
        who_start = 2
    elif current_player == player_2:
        who_start = 1
    
# winner_player = p1 if who_start == 2 else p2
print(f"{current_player} is the winner!")