

# Task 1

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# # Your code here

# if username == valid["username"] and password == valid["password"]:
#     print(f'Welcome, {username}!')
# else:
#     print('Credentials are invalid')


# Task 2
import datetime

def isweekend(date=datetime.datetime.now()):

    weekday = date.weekday()

    return weekday == 5 or weekday == 6

    # if weekday == 5 or weekday == 6:
    #     return True
    # else:
    #     return False

# print(isweekend())
# print(isweekend(datetime.date(2023, 10, 21)))
# print(isweekend(datetime.date(2021, 8, 7)))
# print(isweekend(datetime.date(2021, 8, 8)))
# print(isweekend(datetime.date(2021, 8, 9)))


# Task 3

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# today = datetime.date(2023, 10, 20)
# # Your code here

# if username == valid["username"] and password == valid["password"] or isweekend(today):
#     print(f'Welcome, {username}!')
# else:
#     print('Credentials are invalid')


# if isweekend(today):
#     if username == valid["username"] and password == valid["password"]:
#         print(f'Welcome, {username}!')
#     elif username != valid["username"] and password == valid["password"]:
#         print('Welcome Anonymous!')
#     elif username == valid["username"] and password != valid["password"]:
#         print('Welcome Anonymous!')
#     elif username != valid["username"] and password != valid["password"]:
#         print('Welcome Anonymous!')
# else:
#     if username == valid["username"] and password == valid["password"]:
#         print(f'Welcome, {username}!')
#     elif username != valid["username"] and password == valid["password"]:
#         print('Credentials are invalid')
#     elif username == valid["username"] and password != valid["password"]:
#         print('Credentials are invalid')
#     elif username != valid["username"] and password != valid["password"]:
#         print('Credentials are invalid')


# if username == valid["username"] and password == valid["password"] and isweekend(today):
#     print(f'Welcome, {username}!')
# elif username != valid["username"] and password == valid["password"] and isweekend(today):
#     print('Welcome Anonymous!')
# elif username == valid["username"] and password != valid["password"] and isweekend(today):
#     print('Welcome Anonymous!')
# elif username != valid["username"] and password != valid["password"] and isweekend(today):
#     print('Welcome Anonymous!')
# elif username == valid["username"] and password == valid["password"] and not isweekend(today):
#     print(f'Welcome, {username}!')
# elif username != valid["username"] and password == valid["password"] and not isweekend(today):
#     print('Credentials are invalid')
# elif username == valid["username"] and password != valid["password"] and not isweekend(today):
#     print('Credentials are invalid')
# elif username != valid["username"] and password != valid["password"] and not isweekend(today):
#     print('Credentials are invalid')



# Task 4

# users = [
#     {
#         "name": "Holly",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "password": "joplin"
#     }
# ]



# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")

# Rest of your code here

# def get_user(username, password):

#     u = None

#     for i in users:
#         if username == i['name'] and password == i['password']:
#             # u = i
#             return i

#     print('An error occurred. You are not authorized.')
#     return u

# user = get_user(username, password)

# print(user)
# if get_user(username, password) == None:
# if not get_user(username, password):
# if not user:
#     print('An error occurred. You are not authorized.')


# print(get_user(username, password))

# user = get_user(username, password)


# Task 5

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]



username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

def get_user(username, password):

    u = None

    for i in users:
        if username == i['name'] and password == i['password']:
            # u = i
            return i
    return u


def show_offers(username, password):

    user = get_user(username, password)

    # if user == None or user['type'] == 'Student':
    if not user or user['type'] == 'Student':
        print('We have great courses to offer you!')


show_offers(username, password)