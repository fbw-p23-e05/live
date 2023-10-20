

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def get_user(username, password):
    for i in users:
        if username == i['name'] and password == i['password']:
            return i
    return None


def is_student(user):
    if user and user['type'] == 'Student':
        return True
    else:
        False


def get_module(user, modulename):
    if user and 'modules' in user:
        # if 'modules' in user:
        for i in user['modules']:
            if modulename == i['title']:
                return i
    return None


def show_registration(username, password, modulename):

    user = get_user(username, password)

    module = get_module(user, modulename)

    if user and is_student(user) and module['title'] == modulename:
        print(f'You are registered to the module {modulename}')
    elif user is None or is_student(user) and modulename != module['title']:
        print(f'You did not register to the module {modulename}')
    elif user and user['type'] == 'Teacher':
        print('You are a teacher')


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
