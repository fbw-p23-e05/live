# function will convert string parameter to upper case
def to_upper(txt):

    if not isinstance(txt, str):
        raise TypeError('The argument passed is not a string.')

    return txt.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):

    if not isinstance(str_list, list):
        raise TypeError('The argument passed is not a list.')

    for word in str_list:

        if not isinstance(word, str):
            raise TypeError('The argument passed is not a string.')

        if word.islower():
            return False
    return True

