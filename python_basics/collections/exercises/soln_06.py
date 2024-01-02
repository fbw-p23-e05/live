
# Task 1

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def intersection(lst1, lst2):

    set_1 = set(lst1)
    set_2 = set(lst2)

    # set_inter = set_1 & set_2
    set_inter = set_1.intersection(set_2)

    return list(set_inter)

print(intersection(list_1, list_2))



