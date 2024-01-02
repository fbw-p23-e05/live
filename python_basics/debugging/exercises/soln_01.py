

def get_total(lst):
    # breakpoint()
    # import pdb; pdb.set_trace()

    # __import__('pdb').set_trace()

    index = 0
    total = 0
    while index < len(lst):
        total += lst[index]
        index += 1
    
    # breakpoint()
    # pdb.set_trace()

    print(total)

    return total

# get_total()
get_total([20, 30, 40, 50])


