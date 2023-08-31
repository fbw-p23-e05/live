# ord() - Convert a single unicode character to its integer representation
# always returns an integer
# uni_a = ord('a')
# uni_h = ord('H')
# uni_nine = ord('9')
# uni_and = ord('&')


# print('Unicode rep for a is:', uni_a,
#       'Unicode rep for H is:', uni_h,
#       'Unicode rep for 9 is:',  uni_nine,
#       'Unicode rep for & is:', uni_and)
# print(ord('ę'))

# password = 'admin@%ę'
# encrypted_pass = ''

# for letter in password:
#     encrypted_pass += str(ord(letter))
#     # print(str(ord(letter)))
    
# print(encrypted_pass)


# chr() - converts the integer point to a single Unicode character
# input is always an integer
# always returns a string
letter_a = chr(97)
letter_d = chr(100)

print(letter_a, letter_d)
print(chr(2067))
