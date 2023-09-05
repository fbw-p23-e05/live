"""
Examples for regular expressions using the python re module
"""
import re

# s = 'foo12bar'

# # the first parameter is the regex, the se3cond one is the string.
# print(re.search('123', s))

# # [] - Square brackets

# print(re.search('ba[atz]', 'foobarqux')) # None
# print(re.search('ba[atz]', 'foobazqux')) # Match
# print(re.search('[a-z]', 'F00bar')) 
# print(re.search('[0-9][0-7]', 'foo27bar'))
# print(re.search('[0-9][3-7][0]', 'foo36bar'))
# print(re.search('[^0-5]', '123456@'))


# . - Dot

# print(re.search('foo.bar', 'foozbar')) # Match
# print(re.search('foo.bar', 'foobar')) # None
# print(re.search('f...bar...', 'gfoozbar1234'))

# ^ - Caret 

print(re.search('^foo', 'foobar')) # Match
print(re.search('^foo', 'barfoo')) # None
print(re.search('^The', 'the quick brown fox jumps over The lazy dog')) # Case sensitive

# $ - Dollar

print(re.search('bar$', 'foo bar')) # Match
print(re.search('bar$', 'bar foo')) # None
print(re.search('dog[.]$', 'the quick brown fox jumps over The lazy dogt'))

s = 'A dogmatic dog buys dogecoin to become rich and buy hotdogs every day.'
print(re.search(' dog ', s))
