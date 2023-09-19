
alphabets = 'abcdefghijklmnopqrstuvwxyz'

text = 'Waltz, bad nymph, for quick jigs vex.'

# import string
# alphabets == text_modified
# alphabets_2 = string.ascii_lowercase


def is_pangram(text):

    for i  in alphabets:
        if i not in text.lower():
            return False
    
    return True

# def is_pangram(text):

#     set_alphabets = set(alphabets)
#     set_texts = set(text.lower())

    # return set_alphabets <= set_texts
    # return set_texts >= set_alphabets
    # return set_alphabets - set_texts == set([])

    #     return True
    # else:
    #     return False
    
print(is_pangram(text))

# print(set_alphabets)
# print(set_texts)


