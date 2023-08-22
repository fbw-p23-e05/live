### Objectives

- Assignment operators 
- Number systems 
- Bitwise operations 
- Control Flow

### Assignment Operators

| Operator | Name | Description | Syntax/Example |
|----------|------|-------------|----------------|
| =        | Assignment Operator| It assigns the right hand side expression value to the operand present on the left| a=b+c |
| += | Addition Assignment | The operator adds the left and right operands and assigns the calculated value to the left hand operator.| a = a + b, a += b |
| -= | Subtraction Assignment | The operator subtracts the right operand from the left operand and assigns the result to the left operand. | a = a - c, a -= c |
| *= | Multiplication Assignment |The operator will multiply the left hand side operand by the right hand operand and assign the result to the left hand operand | a = a * c, a *= c |
| /= | Division Assignment | The operator will divide the left hand operand by the right hand operand and assign the result to the left hand operand | a = a / c, a /= c |
| %= | Modulus Assignment | The operator will divide the left hand side by the right hand side and assign the remainder to the left hand operand. | a = a % c, a %= c |
| **= | Exponentiation Assignment | The operator raises the left hand operand by the right hand operand and assigns the result to the left hand operand. | a = a ** 3, a **= 3 |
| //= | Floor Division Assignment | The operator will divide the left hand operand by the right hand operand and assign the minimum value (integer) to the left hand operand | a = a // c, a //= c |


### Number Systems

- Decimal Number System (0,1,2,3,4,5,6,7,8,9)
- Octal Number System (0,1,2,3,4,5,6,7)
- Hexadecimal Number System (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
- Binary Number System (0,1)

#### Binary Number System

- A binary is represented with 0's and 1's.
- The base of binary numbers is 2.
- If we want to store a binary number in a python variable, that number should start with `0b`.

#### Octal Number System

- The base of octal number system is 8.
- The possible digits to be used are 0,1,2,3,4,5,6,7.
- To represent an octal number in Python, the number should start with `0o`

#### Decimal Number System

- The base of the decimal number system is 10.
- The possible digits that can be used are 0,1,2,3,4,5,6,7,8,9.
- **The default number system followed by Python.**

#### Hexadecimal Number System

- The base of the hexadecimal number system is 16.
- The possible digits that can be used are `0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F`
- To represent a hexadecimal number in Python, the number should start with `0x`.

### Converting from Decimal to other number systems

- These functions take an integer and return a string.
- We use built-in Python functions to convert decimal numbers into other number systems.
- `bin()` will convert to binary.
- `oct()` will convert to octal.
- `hex()` will convert to hexadecimal.


### Bitwise Operators

- Python bitwise operators are used to perform bitwise calculations on integers.
- The integer is converted to binary format and the operations performed bit by bit.
- Python bitwise operators only work on integers and the final output is returned in decimal format.
- Sometimes known as binary operators.

| Bitwise Operator | Description | Example |
|------------------|-------------|---------|
| `&` | Bitwise AND operator | 10 & 7 = 2 |
| `|` | Bitwise OR operator | 10 `|` 7 = 15 |
| `^` | Bitwise XOR operator (Exclusive OR) | 10 ^ 7 = 13 |
| `~` | Bitwise Ones' Compliment Operator | ~10 = -11 |
| `<<` | Bitwise Left Shift Operator | 10 << 2 = 40 |
| `>>` | Bitwise Right Shift Operator | 10 >> 1 = 5 |



##### Extra Resources & Links
 
https://sid-sharma1990.medium.com/number-system-in-python-11b0a10ea67b

https://byjus.com/maths/number-system/#:~:text=A%20number%20system%20is%20defined,algebraic%20structure%20of%20the%20figures.

https://realpython.com/python-bitwise-operators/#bitwise-shift-operators


