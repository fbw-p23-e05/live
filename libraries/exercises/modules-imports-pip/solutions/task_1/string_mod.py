def concat(str_1: str, str_2: str) -> str:
    """Concatenates two strings."""
    return str_1 + str_2
    
    
def create_string(char_list: list) -> str:
    """Create a string form a list."""
    phrase = ""
    for letter in char_list:
        phrase += letter
    return phrase
    # return "".join(char_list)


def check_digit(str_1: str) -> bool:
    """Check if string contains at least one digit."""
    for char in str_1:
        if char.isdigit():
            print("There is a digit in your string!")
            return True
    print("No digits!")
    return False
