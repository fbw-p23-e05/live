

### Task 1: What is the maximum possible number with 4 bits?
# 0, 1, 2, ......, 9

# decimal = 2**4 - 1
# print(decimal) 
# print(bin(decimal))

# decimal = 10**4 - 1
# print(decimal) # 9999
# #print(bin(decimal))


### Task 2: Check if the following numbers are even or odd with the bitwise and operator

# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
# num6 = 600

# 0b1 & 1
# 0b10 & 1 = 
# 0b11 & 1 = 

# 10 & 01

# 0

# 1001011000 & 0000000001

# 000000000



# print(num1, bin(num1), num1 & 1)
# print(num2, bin(num2), num2 & 1)
# print(num3, bin(num3), num3 & 1)
# print(num4, bin(num4), num4 & 1)
# print(num5, bin(num5), num5 & 1)
# print(num6, bin(num6), num6 & 1)


### Task 3: Change the value with the xor operator of the following numbers

# a = 1
# b = 2

# c = a ^ b
# print(bin(a), '^',bin(b), ' = ', bin(c)) # 0b1 ^ 0b10 = 0b11

# d = c ^ b
# print(bin(c), '^',bin(b), '= ', bin(d)) # 0b11 ^ 0b10 = 0b1


# 01 ^ 10

# 01
# 10
# ----
# 11
# 10
# ----
# 1


### Task 4: Swap the values of a and b

# a = 1
# b = 2

# print('before swap: a =', a, ', b =', b)

# c = a ^ b
# a = c ^ a
# b = c ^ b

# print('after swap: a =', a, ', b =', b)


### Task 5: Left shift a number by certain number of bits


# num = 1
# shift_amount1 = 1
# shift_amount2 = 2
# shift_amount3 = 3
# shift_amount4 = 4

# print(num << shift_amount1)  # shift left by 1 bit
# print(num << shift_amount2)  # shift left by 2 bits
# print(num << shift_amount3)  # shift left by 3 bits
# print(num << shift_amount4)  # shift left by 4 bits

# print(bin(num << shift_amount1)) # shift left by 1 bit
# print(bin(num << shift_amount2)) # shift left by 2 bits
# print(bin(num << shift_amount3)) # shift left by 3 bits
# print(bin(num << shift_amount4)) # shift left by 4 bits


# print(num * 2**shift_amount1)
# print(num * 2**shift_amount2)
# print(num * 2**shift_amount3)
# print(num * 2**shift_amount4)



### Task 6: Right shift a number by a certain number of bits

num = 28  # 11100 in binary
shift_amount = 2
result = num >> shift_amount
print(result)  # Output: 7 (111 in binary)

