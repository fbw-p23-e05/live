
# Task 1

participants = ['Brian', 'Britney', 'Ben']

scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}


def get_score(name):
    if name in participants:
        print(f'{name} scored {scores[name.lower()]} points')
    else:
        print(f'{name} did not participate')


for i in participants:
    get_score(i)

# get_score('Paul')

# get_score('Britney')


