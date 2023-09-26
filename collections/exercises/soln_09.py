
# Task 1

dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}

# t = 0

# for i in dict1:
#     t += dict1[i] * dict2[i]


# print(t)
   

result = sum(dict1[key] * dict2[key] for key in dict1)

print(result)



