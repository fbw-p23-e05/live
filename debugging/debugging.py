def sum_of_list(my_list):
    print(my_list)
    flatten_list = []
    for item in my_list: 
        print(item)
        if isinstance(item, list):
            flatten_list.extend(item)
        else:
            flatten_list.append(item)
    return sum(flatten_list)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_list(list_1)
