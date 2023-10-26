

def BubbleSort(list):

    swaps = False

    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            swaps = True

    if swaps == True:
        return BubbleSort(list)

    return list

print(BubbleSort([34, 40, 2, 7, 20, 100, 21]))
