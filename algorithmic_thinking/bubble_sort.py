

my_list = [64, 34, 25, 12, 22, 11, 90]

# my_list = [64, 34]

# my_list[0], my_list[1] = my_list[1], my_list[0]

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#             print(arr)


# bubble_sort(my_list)
# print("Sorted list:", my_list)

# x, y = y, x

my_list = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(our_list):
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True

    return our_list


bubble_sort(my_list)
print("Sorted list:", my_list)

