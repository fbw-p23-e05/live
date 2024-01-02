plain_text = input("What is the message?: ")
shift_key = int(input("What is key?:"))
cipher_text = ''

# iterate over the given text
for letter in plain_text:
    
    # checking for a space
    if letter == " ":
        cipher_text += " "
    
    # check if the letter is uppercase
    elif letter.isupper():
        
        # get integer rep of character in the unicode format
        char_position = ord(letter)
        
        # add the shift to the unicode integer
        new_pos = (char_position + shift_key - 65) % 26 + 65
        
        # use the new integer to get the cipher character
        new_letter = chr(new_pos)
        
        # add the new character to the cipher text
        cipher_text += new_letter 
        
    else:
        char_position = ord(letter)
        new_pos = (char_position + shift_key - 97) % 26 +97
        new_letter = chr(new_pos)
        cipher_text += new_letter    
        
print(cipher_text)
