

my_list = [38, 27, 3, 43, 3, 3, 3, 9, 82, 10]


def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sorted_list = merge_sort(my_list)
print("Sorted list:", sorted_list)


# sorted()

# my_list.sort()






