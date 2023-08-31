# Character Encoding

- Encoding schemes are used to convert characters that we use daily to machine language. 
- ASCII and Unicode are the most popular encoding shemes.
- ASCII encodes symbols, letters, digits, etc.
- Unicode encodes special texts from different languages as well.
- ASCII is a subset of Unicode

## The ASCII characters

- ASCII - American Standard Code for Information Interchange and is used for electronic communication.
- It uses integers to encode:
    - numbers(0-9)
    - uppercase alphabet (A-Z)
    - lowercase alphabet (a-z)
    - symbols (!,@,#)

- integers are easy to store in electronic devices.

a - 97 
97 + 25 = 122
z - 122

- The major disadvantage of ASCII is that it can only represent 256 different characters

**Use `man ascii` in your terminal to display the ASCII table.**

## The Unicode characters

- Unicode - Universal Character Set and is maintained by the Unicode Consortium.
- Unicode represents a vast ocean of characters, formulas, mathematical symbols and texts from different languages for example: Latin, Greek, Armenian, Arabic, Hebrew, etc.
- It also represents text that can be written from right to left, for example: Arabic and Hebrew.
- Unicode Transformation Format(UTF) is the type of Unicode encoding scheme. 
- The types of encoding schemes that are currently used:
    - UTF-7 - 7 bits
    - UTF-8 - 8 bits
    - UTF-16 - 16 bits
    - UTF-32 - 32 bits

- The requirement of Unicode is for the internationalization and localization of computer software and is also used for operating systems, XML, Java, etc.

