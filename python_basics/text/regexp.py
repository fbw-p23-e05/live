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

# print(re.search('^foo', 'foobar')) # Match
# print(re.search('^foo', 'barfoo')) # None
# print(re.search('^The', 'the quick brown fox jumps over The lazy dog')) # Case sensitive

# $ - Dollar

# print(re.search('bar$', 'foo bar')) # Match
# print(re.search('bar$', 'bar foo')) # None
# print(re.search('dog[.]$', 'the quick brown fox jumps over The lazy dogt'))

# s = 'A dogmatic dog buys dogecoin to become rich and buy hotdogs every day.'
# print(re.search(' dog ', s))

"""
* - Star - zero or more occurrences.
"""

# pattern = 'foo-*bar'
# print(re.search(pattern, 'foobar'))
# print(re.search(pattern, 'foo-bar'))
# print(re.search(pattern, 'foo-------bar'))

# print(re.search('foo.*bar', '3 foo $@huthtyer & bar #'))

# + - Plus - matches one or more occurrences

# pattern = 'foo-+bar'

# print(re.search(pattern, 'foobar'))
# print(re.search(pattern, 'foo-bar'))
# print(re.search(pattern, 'foo-------bar'))
# print(re.search(pattern, 'foo---baxr'))
# print(re.search(pattern, 'foo------barzxtytergne'))


"""
'?' - matches zero or one occurrences.
"""

# pattern = 'foo-?bar'

# print(re.search(pattern, 'foobar')) # Match
# print(re.search(pattern, 'foo-bar')) # Match
# print(re.search(pattern, 'foo--bar')) # None - more than one '-'

# print(re.search('foo[3-6]?bar', 'foo4bar')) # Match 

# {} - Braces

# pattern1 = 'x-{4}x'

# print(re.search(pattern1, 'x---x'))
# print(re.search(pattern1, 'x----x')) # Match
# print(re.search(pattern1, 'x----6x'))

# pattern2 = 'x-{4,6}x' + pattern1
# print(re.search(pattern2, 'x---x'))
# print(re.search(pattern2, 'x----x')) # Match
# print(re.search(pattern2, 'x----6x'))
# print(re.search(pattern2, 'x------x')) # Match
# print(re.search(pattern2, 'x-----x')) # Match

# | - Alternation (Vertical Bar)

# pattern = 'a|g|t'

# print(re.search(pattern, 'age is just a number'))
# print(re.search(pattern, 'hurd tnv gae'))
# print(re.search(pattern, '1234 bek rdsa'))

# print(re.search('[7|d|0-5|b]xyz', '15dxyz, 7xyze'))


# () -Group 

pattern = '(b|t|w)ool'

print(re.search(pattern, 'boolean'))
print(re.search(pattern, 'tools'))
print(re.search(pattern, 'woolie mammoth'))
print(re.search(pattern, 'fool'))

pattern2 = '(foo)[0-9]\1'

print(re.search(pattern2, 'foo6bar'))
print(re.search(pattern2, 'too8bar'))
print(re.search(pattern2, 'foo4 bar it'))

'[0-9]{5}([A-Z]{2})'


