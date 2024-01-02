play = True

while play == True:
    name = input('What is your name?: ')
    print('Hey', name)
    print('Welcome to the Quest Game!')
    # Use \n to print the next statements on a new line
    print('1. Wonderland \n2. Lala land \n3. Space')
    # Wrap the input method with int() to convert to an integer
    choice = int(input('Where would you like to go today?: '))
    if choice == 1:
        print('Welcome to Wonderland!')
        print('There is lots to do here, but first you must say beetle juice 3 times.')
        print('1. Say beetle juice to continue. \n2. Quit game')
        first_choice = int(input('Would you like to continue?: '))
        if first_choice == 1:
            for i in range(3):
                # print('Beetle juice.')
                input()
            print('Great choice! Let us see how far you get.')
            colour = input('What is the colour of your fear (yellow or red): ')
            if colour == 'yellow' or 'blue':
                print("That's very mild you seem to fear nothing")
            elif colour == 'red':
                print('You have a lot of fears young one!')
            else:
                print('Make the correct choice.')
        else:
            print('Thank you for playing!')
            play = False
    elif choice == 2:
        print('Welcome to Lala land!')
    
    
    
