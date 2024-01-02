with open('../data/task4.txt') as file:
    file.seek(1622)  # telling the file which position to start from
    print(file.read())  # use read method to print 13 positions (1634)

    print(file.read()[1622:1635])  # alternative
    