
# Task 1

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

# def digit_filter(list):

    # e = []

    # for i in list:
    #     for j in i:
    #         if j.isdigit():
    #             e.append(i)
    #             break    

    # for i in e:
    #     list.remove(i)  

    # return list


def digit_filter(list):

    e = []

    for i in list:
        if not any(j.isdigit() for j in i):
            e.append(i)
    
    return e

print(digit_filter(l33t))

# print(l33t)





