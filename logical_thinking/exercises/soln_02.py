# Task 1

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


def module_registered(user, modulename):
        for i in user['modules']:
            if i["title"] == modulename:
                return i
        return None


def show_registration(username, password, modulename):

    user = get_user(username, password)

    # module = get_module(user, modulename)
    # module = module_registered(user, modulename)

    if is_student(user) and module_registered(user, modulename):
        print(f"You are registered to the module {modulename}.")
    elif not user or is_student(user):
        print(f"You did not register to the module {modulename}.")
    else:
        print(f"You are a teacher.")


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)


# Task 2

def has_completed_module(username, password, modulename):

    user = get_user(username, password)

    if user and is_student(user):
        module = module_registered(user, modulename)
        if module and module["completed"]:
            print(f"You have completed the module {modulename}.")
            return
    if not user or is_student(user):
        print(f"You did not complete the module {modulename}.")


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# modulename = input("What module do you want to check? ")
# show_registration(username, password, modulename)
# has_completed_module(username, password, modulename)


# Task 3

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]

def get_module(modulename):
    for i in modules:
        if i["name"] == modulename:
            return i
    return None


def is_anonymous(user):
    if not user:
        return True
    else:
        return False
    # return not user


def has_no_requirement(module):

    if module:
        if 'requirement' not in module:
            return True
    return False


def module_completed(user, modulename):

    for i in user["modules"]:
        if i["title"] == modulename and i["completed"]:
            return i
    return None


def meets_requirement(user, module):

    if module:
        if not module_registered(user, module["name"]) and (has_no_requirement(module) or module_completed(user, module["requirement"])):
            return True
    return False   


def may_enroll(username, password, modulename):

    user = get_user(username, password)

    # module = get_module(user, modulename)
    module = get_module(modulename)

    if is_anonymous(user) and has_no_requirement(module):
        return True
    elif is_student(user) and meets_requirement(user, module):
        return True
    else:
        return False
    

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")

