

dict = {'vendor_name':'Amazon Inc.', 'industry':'Ecommerce'}

# dict2 = list([k,j] for k,j in (dict.keys(), dict.values()))

# dict2 = list(k + ', ' + j for k,j in (dict.keys(), dict.values()))

dict2 = list([k,j] for k,j in (dict.keys(), dict.values()))

# new = tuple((k, j) for k, j in (dict.keys(), dict.values()))
# str = []
# for part in new:
#     for second_part in part:
#         str.append(second_part)
# print(tuple(str))

for i in dict2:
    print(i)
print(dict2)
print(type(dict2))

# a=3
# b=4

# tup = (a,b)

# print(type(tup))