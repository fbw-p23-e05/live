
# Task 1

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

def has_hits(author):
    for user in users:
        if user['name'] == author:
            for i in user['items']:
                if 'reads' in i:
                    if i['reads'] > 1000:
                        return True
    return False


# print("Clark", has_hits("Clark"))
# print("Peter", has_hits("Peter"))
# print("Samantha", has_hits("Samantha"))
# print("Mathilda", has_hits("Mathilda"))
# print("Mario", has_hits("Mario"))



# Task 2


def author_average_reads(author):

    total = 0
    n = 0

    # for user in users:
    #     if user['name'] == author:
    #         if user['type'] != 'Reviewer':
    #             if user['items'] != []:
    #                 for i in user['items']:
    #                     if 'reads' in i:
    #                         if i['status'] == 'Published':
    #                             total += i['reads']
    #                             n += 1

    for user in users:
        if user['name'] == author and user['type'] != 'Reviewer' and user['items'] != []:
            for i in user['items']:
                if 'reads' in i and i['status'] == 'Published':
                    total += i['reads']
                    n += 1
    if n == 0:
        return 0
    else:
        return int(total / n)            
                    

# print("Clark", author_average_reads("Clark"))
# print("Peter", author_average_reads("Peter"))
# print("Samantha", author_average_reads("Samantha"))
# print("Mathilda", author_average_reads("Mathilda"))
# print("Mario", author_average_reads("Mario"))


# Task 3

# def author_is_popular(author):
#     for user in users:
#         if user['name'] == author and 'items' in user and user["items"] != []:
#             return (sum(i['reads'] for i in user['items'] if i['status'] == 'Published') / len(user['items'])) > 1000
        
#     return False

def get_user(author):
    for user in users:
        if user['name'] == author:
            return user       
    return None


def author_is_popular(author):

    user = get_user(author)

    return bool(user and (user["items"] != [] and (sum(i['reads'] for i in user['items'] if i['status'] == 'Published') / len(user['items'])) > 1000))


print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))



# Extra
# user = get_user(author)

    # if user:
    #     return (user["items"] != [] and (sum(i['reads'] for i in user['items'] if i['status'] == 'Published') / len(user['items'])) > 1000)

    # return False