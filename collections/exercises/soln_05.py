
# Task 1

strings = ['Digital', 'Career', 'Institute', 'Lecture', 'P', 'Exercise', 'Zoom']

# def count(txt):
#     return len(set(txt))

def unique_char_sort(text):

    # s = sorted(text, key=count)

    text.sort(key = lambda txt: len((set(txt))))

    return text


print(unique_char_sort(strings))



# def calculate(x, y):
#     return x + y


# l = lambda x, y: x + y


# print(calculate(10, 20))
# print(l(100, 200))



text = 'Digital'

print(len(list(text)))
print(len(set(text)))