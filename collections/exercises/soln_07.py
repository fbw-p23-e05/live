
# Task 1

# person = {'name': 'Bart Simpson', 'address': '742 Evergreen Terrace'}


# print(f"{person['name']}, {person['address']}")


# Task 2

# bart = {'name': 'Bart Simpson'}

# homer = {'name': 'Homer Simpson'}

# address = {'address': '742 Evergreen Terrace'}

# bart.update(address)
# homer.update(address)

# print(bart['address'])
# print(homer)


# Task 3


# ages = {'Peter': 36, 'Robin': 29, 'Michael': 33}

# for name,age in ages.items():
#     print(f'{age} is {name} years old')


# Task 4


animals = {'Alligator': 4, 'Tiger': 7, 'Parrot': 3, 'Hamster': 10, 'Dolphin': 1}

# e = []
e = {}

# for i,j in animals.items():
#     if i.endswith('r'):
#         e.append(i)

for i,j in animals.items():
    # if not i.endswith('r'):
    if i[-1] != 'r':

        # e[i] = j
        e.update({i:j})

# for i in e:
#     animals.pop(i)

print(e)
# print(animals)

