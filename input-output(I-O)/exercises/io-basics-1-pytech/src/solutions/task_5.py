with open('../data/task5.txt') as file:
    print(file.readline())
    print(file.tell() - 1)
    
    char_list = file.readline()
    counter = 0
    for char in char_list:
        counter += 1
    print(counter - 1)
    