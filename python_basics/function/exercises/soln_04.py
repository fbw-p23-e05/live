

def decorator(func):
    def inner(*args, **kwargs):
        return 'something'
    return inner


def decorator(text, num):
    def wrapper(func):
        def inner(*args, **kwargs):
            return 100
        return inner
    return wrapper


# Task 1

# def make_bold(func):
#     def inner():
#         return f'<strong>{func()}<strong>'
#     return inner

# @make_bold
# def get_html_greeting():
#     return 'Hello world!'

# print(get_html_greeting())

# Task 2

# def make_bold(func):
#     def inner(*args, **kwargs):
#         return f'<strong>{func(*args, **kwargs)}<strong>'
#     return inner

# @make_bold
# def get_custom_html_greeting(first, last):
#     return f'Hello, {first}, {last}!'

# print(("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))
# print(get_html_greeting())

# Task 3

# def make_bold(func):
#     def inner(*args, **kwargs):
#         return f'<strong>{func(*args, **kwargs)}<strong>'
#     return inner

# @make_bold
# def get_full_name(first, last):
#     return f'{first} {last}'


# def make_italics(func):
#     def inner(*args, **kwargs):
#         return f'<em>{func(*args, **kwargs)}<em>'
#     return inner

# def make_paragraph(func):
#     def inner(*args, **kwargs):
#         return f'<p>{func(*args, **kwargs)}<p>'
#     return inner

# @make_paragraph
# @make_italics
# def get_custom_html_greeting(first, last):
#     return f'Hello, {get_full_name(first, last)}!'

# print(get_custom_html_greeting('Alex', 'Jordan'))
# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))


# Task 4

def make_italics(func):
    '''Returns string with a <em> tag at the start and end of it.'''
    '''Makes the string italics.'''
    def inner(*args, **kwargs):
        return f'<em>{func(*args, **kwargs)}<em>'
    return inner

def make_paragraph(func):
    '''Returns string with a <p> tag at the start and end of it.'''
    def inner(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}<p>'
    return inner

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    '''Adds greeting at the start of a person's name'''
    '''Greets a person with his/her full name.'''
    return f'Hello, {get_full_name(first, last)}!'

def wrap_with(tag):
    '''Returns string with a specific tag at the start and end of it.'''
    def make_bold(func):
        def inner(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}<{tag}>'
        return inner
    return make_bold

@wrap_with(tag='strong')
def get_full_name(first, last):
    '''Retuns full name of a person.'''
    return f'{first} {last}'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

