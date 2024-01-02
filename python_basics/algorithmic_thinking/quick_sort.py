

my_list = [3, 6, 8, 10, 1, 2, 1]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    

    # pivot = arr[len(arr) // 2]
    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

sorted_list = quick_sort(my_list)
print("Sorted list:", sorted_list)
    

# x = 21

# y = x // 2

# print(y)




