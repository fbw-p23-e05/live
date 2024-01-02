
# Task 1

swap_list = [23, 65, 19, 90]

def swap_items(list, idx1, idx2):

    list[idx1], list[idx2] = list[idx2], list[idx1]

    return list

print(swap_items(swap_list, 1, 3))