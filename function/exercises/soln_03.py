

# Task 1

settings = {'title': 'My original title'}


def change_site_title(dtext):
    '''Changes the value of title.'''

    settings['title'] = dtext

#     # return settings['title']

# print(settings['title'])
# change_site_title('A new fancy title')
# print(settings['title'])


# Task 2

default_settings = {'title': 'My original title'}


def get_title(dtext=default_settings):
    '''Returns the value of the title.'''

    return dtext['title']


# print(get_title(settings))
# print(get_title())
# change_site_title("A new fancy title")
# print(get_title(settings))

# print(get_title())


# Task 3

# settings['pages'] = []

# default_settings['pages'] = []

# # print(settings)


# def get_pages(settings=default_settings):

#     return settings['pages']


# def add_page(page, settings=default_settings):

#     settings['pages'].append(page)


# home = {"title": "Home", "path": "/"}
# add_page(home)
# print(get_pages())
# print(get_pages(settings))
# about = {"title": "About", "path": "/about/"}
# add_page(about, settings)
# print(get_pages())
# print(get_pages(settings))


# Task 4

# def print_user_profile(gender='female', first=None, last='Doe', pictures=[]):

def print_user_profile(gender='female', first=None, last='Doe', pictures=None):

    if first == None:
        if gender == 'male':
            first = 'John'
        elif gender == 'female':
            first = 'Jane'

    # if len(pictures) != 0:
    #     if pictures[0] != 'common_header.png':
    #         pictures.insert(0, 'common_header.png')
    # elif len(pictures) == 0:
    #     pictures.insert(0, 'common_header.png')

    if pictures == None:
        pictures = []
        pictures.append('common_header.png')
    else:
        pictures.insert(0, 'common_header.png')

    print(f'The user {first} {last} has the following pictures:')

    for pic in pictures:
        print(pic)


test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)



