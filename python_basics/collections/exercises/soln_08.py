
# Task 1

books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}


def best_sellers(dict_books):

    s = sorted(dict_books.items(), key=lambda x: x[1], reverse=True)

    # for i in s[:3]:
    #     # print(i[0] + ': ' + str(i[1]))
    #     print(f'{i[0]}: {i[1]}')

    for i in range(3):
    # print(i[0] + ': ' + str(i[1]))
        title, sales = s[i]

        print(f'{i+1}.{title}: {sales}')

    # print(s)

    # return s

best_sellers(books)






