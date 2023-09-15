# Task 1
'\d+$'

# Task 2

import re

# all_nums = re.findall('\d{1,3}', 'Exercises number 1, 12, 13, and 345 are important')

# for i in all_nums:
#     print(i)

# Task 3

'(fox)*(dog)*(horse)*'

# Task 4

# text = 'The quick brown fox jumps over the lazy dog.'

# word = re.search('fox', text)

# print('Found the word fox at location:', word.span())


# Task 5

# text = 'Python exercises, PHP exercises, C# exercises'

# print(re.findall('exercises', text))


# Task 6

# text = 'The quick brown fox jumps fox over the fox lazy dog.'

# words = re.finditer('fox', text)

# for i in words:
#     print('Found the word fox at location:', i.span())


# Task 7

# text = 'The quick brown fox jumps fox over the fox lazy dog.'

# text_underscore = re.sub('\s', '_', text)

# text_space = re.sub('_', ' ', text_underscore)

# print(text_underscore)
# print(text_space)


# Task 8

# url = 'https://google.com/search?=date=2023/12/24'

# event_date = re.search('\d{4}/\d{2}/\d{2}', url)

# print(event_date)



# Task 9

# url = 'https://google.com/search?=date=2023-12-24'

# event_date = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', url)

# print(event_date)


# Task 11

# all_nums = re.findall('\d+', 'Exercises number 1, 12, 13, and 345444 are important')

# print(all_nums)


# Task 12

# text = 'The quick brown fox jumps fox over the fox lazy dog.'

# all_words = re.findall('\b[ae]\w*', text)

# print(all_words)


# Task 13

# all_nums = re.finditer('\d+', 'Exercises number 1, 12, 13, and 345444 are important')

# for i in all_nums:
#     print(f'Found {i.group()} at position {i.span()}')

# print(all_nums)


# Task 14

# text = 'The quick brown Road fox jumps fox over the fox lazy dog.'

# print(re.sub('Road', 'Rd', text))


# Task 15

# text = 'The quick brown fox jumps fox over the fox lazy dog, apple, and eagle....'

# new_text = re.sub('[\s,.]', ':', text)

# print(new_text)


# Task 16

text = 'The quick brown fox jumps fox over the fox lazy dog, apple, and eagle....'

new_text = re.subn('[\s,.]', ':', text, count=2)

print(new_text[0])


