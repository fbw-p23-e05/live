

# Task 1

def sum_series(n):
    '''Returns the sum of the positive integers in a series.'''
    if n <= 0:
        return 0
    else:
        return n + sum_series(n-2)

# print(sum_series(7))
# print(sum_series(8))
# print(sum_series(15))


# Task 2

# test_data1 = [
#     1,
#     [1, 2],
#     [1, [2, 3]],
#     [1, [2, [3, 4]]],
#     [1, [2, [3, [4, 5]]]],
# ]
# test_data2 = [
#     [1, [[2, 6], [3, 4]]],
#     [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
#     [1, [2, 3]],
#     [1, 2],
#     1,
# ]


# def drill_sum(n_list):
#     '''Returns sum of integers in a given list of lists.'''
#     if isinstance(n_list, int):
#         return n_list
#     elif n_list == []:
#         return 0
#     else:
#         return drill_sum(n_list[0]) + drill_sum(n_list[1:])

# print(drill_sum(test_data1))
# print(drill_sum(test_data2))


# Task 3

test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]


def count_pages(p_list):
    '''Counts the amount of pages in a given list of dictionaries.'''

    total = 0

    for i in p_list:
        if 'pages' not in i:
            total = total + 1
        else:
            total = total +1 + count_pages(i['pages'])

    return total

print(count_pages(test_data1))