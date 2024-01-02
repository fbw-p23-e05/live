
# Task 1

def QuickSort(list, low=0, high=-1):
    if high == -1:
        high = len(list) - 1 # low = 0, high = 7

    if low < high:
        pi = Partition(list, low, high) # list, low = 0, high = 7 => 6
        QuickSort(list, low, pi - 1) # list, low = 0, 5
        QuickSort(list, pi + 1, high)

    return list


def Partition(list, low, high): # list, low = 0, high = 7
    pivot = list[high]  # 4
    i = low - 1 # i = -1

    for j in range(low, high): # range(0, 7)
        if list[j] < pivot: # 3 < 4
            i += 1 # i = 0
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1] # i = 5, 

    return i + 1 # i = 6


# print(QuickSort([20, 3, 1033, 55, 8, 32, 77, 5]))


#!/usr/bin/env python

# from quicksort import quicksort


def main():
    a = [3, 7, 2, 8, 4, 6, 9, 1, 4]
    b = QuickSort(a)
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

