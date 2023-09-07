import re

"""
findall() - returns a list of strings containing all the matches.
"""

# Extract number from a string

# string = 'Hello, 3 my pho45ne 12 number is 07534 call me at 6.'
# pattern = '[0-9]+'

# result = re.findall(pattern, string)
# print(result)

"""
split() - Splits the string where there is a match and returns a list of where the splits have occured.
"""

# string = 'Thirteen:13 Seventy-Nine:79 One hundred:100'
# pattern = '\d+' #'[0-9]+'

# result = re.split(pattern, string)
# print(result)

"""
sub() - returns a string where matched occurrences have been replaced with the content of th
replace variable.
"""

# string = 'abc 34 de 56 fgh 789'
# pattern = '\s' # Special sequence for whitespace
# replace = ''

# result = re.sub(pattern, replace, string)
# print(result)

"""
subn() - returns a tuple of 2 items containing the new string and the number of substitutions made.
"""

# string = 'abc 34 de 56 fgh 789'
# pattern = '\s'
# replace = ''

# result = re.subn(pattern, replace, string)
# print(result)


"""
search() - it identifies the first occurrence or match and returns Match object if there is a match
and None if there is no match.
"""

# string = "Reglot1Ex fis a lot2 of funlot3! lot4"
# pattern = 'lot[0-9]'

# result = re.search(pattern, string)
# print(result)


# Match object
"""
group() - returns the part of the string where the match is found.
"""

# string = '38765 456, 3456 2222'
# pattern = '(\d{3}) (\d{2})' # 345 33
# regex = re.compile(pattern)
# groups = regex.groups
# print(groups)
# result = re.search(pattern, string)
# print(result.group())

"""
r/R - raw string.
"""

string = '\n and \r are escape sequences.'
pattern = R'[\n\r]'

result = re.findall(pattern, string)
print(result)
