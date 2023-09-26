
# Task 1

natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}

# e = {}

# for i in natural_case:
#     k = i.replace(' ', '_').lower()

#     # e[k] = natural_case[i]

#     e.update({k: natural_case[i]})

# print(e)

result = {key.replace(' ', '_').lower():value for key,value in natural_case.items()}

print(result)



