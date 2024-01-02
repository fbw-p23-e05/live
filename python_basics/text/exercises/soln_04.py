import re

# result = re.search('[a-zA-Z0-9]+', 'Abcd1234')

# print(result)


# result = re.search('[a-z]+_[a-z]+', 'abcd1234')

# print(result)

# Task 1 

'[a-zA-Z0-9]'

# Task 2 

'ab*'

# Task 3

'ab+'

# Task 4

'ab?'

# Task 5

'ab{3}'

# Task 6

'ab{2,3}'

# Task 7

'[a-z]+\_[a-z]+'

# Task 8

'[A-Z][a-z]+'

# Task 9

'(a.+)b$' 'or' '\w*(a.+)b$'

# Task 10

'^\w+'

# Task 11

'\w+[.,?!]*$' 'or' '\w+[.,?!]?$'

# Task 12

'\w*z\w*'

# Task 13

'[a-yA-Y]+z+[a-yA-Y]+'

# Task 14

'\w+'

# Task 15

'^7'

# Task 16

ip_address = '024.505.0010.080'

new_ip = re.sub('0*(\d*)', r'\1', ip_address)

print(new_ip)


#  \bdog\b
#  \bdog[\.| ]
#  \sdog\W
#  \sdog[^a-zA-Z]



