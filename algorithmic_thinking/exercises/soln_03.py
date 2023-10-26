

# Task 1

# list_1 = [3] 

# list_2 = list_1 * 150

# print([None] * 50)




def MergeSort(list, left=0, right=-1):
    if right == -1:
        right = len(list) - 1

    if right > left:
        middle = int(left + (right - left)/2)
    # mergesort both halves
        MergeSort(list, left, middle)
        MergeSort(list, middle+1, right)
    # merge the halves
        Merge(list, left, middle, right)

    return list


def Merge(list, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

# Create temp lists
    Left = [None] * n1
    Right = [None] * n2

# Copy data to temp lists Left and Right
    for i in range(n1):
        Left[i] = list[left + i]

    for j in range(n2):
        Right[j] = list[middle + 1 + j]

# Merge the temp lists back

# Initial index of first sublist
    i = 0

# Initial index of second sublist
    j = 0

# Initial index of merged sublist
    k = left

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            list[k] = Left[i]
            i += 1
        else:
            list[k] = Right[j]
            j += 1   
        k += 1

# Copy the remaining elements of
# Left, if there are any
    while i < n1:
        list[k] = Left[i]
        i += 1
        k += 1

# Copy the remaining elements of
# Right, if there are any
    while j < n2:
        list[k] = Right[j]
        j += 1
        k += 1

# print(MergeSort([23, 80, 45, 2, 103, 20034, 10, 507]))


#!/usr/bin/env python

# from mergesort import mergesort


def main():
    a = [3, 7, 2, 8, 4, 6, 9, 1, 4]
    b = MergeSort(a)
    # We check if the result is correct
    c = [1, 2, 3, 4, 4, 6, 7, 8, 9]
    if len(b) != len(c):
        print("Failed - length is incorrect!")
        print(b)
        print(c)
        return
    for i in range(0, len(c) - 1):
        if b[i] != c[i]:
            print("Failed - order is incorrect!")
            print(b)
            print(c)
            return
    print("Congratulations! No error detected.")


if __name__ == "__main__":
    main()
