with open('../data/task6.txt', encoding='utf-8') as file:
    # read the first line
    # line = file.readline()
    
    # create an empty list to store line lengths
    line_len = []
    
    # # start  a loop for the size of the file
    # while line:
    #     # get current position of the file
    #     # subtracting the whitespace/line break
    #     # 
    #     line_len.append(file.tell() - 1 - sum(line_len))
    #     # go to the next line
    #     line = file.readline()
    # print(line_len)

    content = file.readlines()
    for line in content:
        counter = 0
        for char in line:
            counter += 1
        line_len.append(counter - 1)
    print(line_len)
