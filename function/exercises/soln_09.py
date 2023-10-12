
# Task 1


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subject_marks.sort(key=lambda x: x[1])
# print(subject_marks)


# Task 2

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_nums = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_nums)

# Task 3


# def protected(func):
#     '''Validates user to execute the function it decorates with his/her username and password.'''
        # username = input('Enter username: ')
#         # password = input('Enter password: ')
#         return lambda : print('You are not authorized') if input('username: ') and input('password: ') != 'admin' else func()

# def public():
#     print("Hello World!")

# @protected
# def private():
#     print("Welcome, admin!")

# public()
# private()


# Task 4

def wrap_with(tag):
    '''Returns string with a specific tag at the start and end of it.'''
    def make_bold(func):    
        return lambda *args, **kwargs: f'<{tag}>{func(*args, **kwargs)}<{tag}>'      
    return make_bold

@wrap_with(tag='p')
@wrap_with(tag='em')
def get_custom_html_greeting(first, last):
    '''Adds greeting at the start of a person's name'''
    '''Greets a person with his/her full name.'''
    return f'Hello, {get_full_name(first, last)}!'

@wrap_with(tag='strong')
def get_full_name(first, last):
    '''Retuns full name of a person.'''
    return f'{first} {last}'


print(get_custom_html_greeting("James", "Brown"))
