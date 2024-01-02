# Caesar Cipher

In cryptography, a Caesar cipher, also known as shift cipher, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet.

![Caesar Cipher](https://media.geeksforgeeks.org/wp-content/uploads/ceaserCipher.png)

The cipher illustrated above uses a left shift of three, so that each occurrence of E in the plaintext becomes B in the ciphertext.

The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

> **Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ**

> **Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW**

When encrypting, a person looks up each letter of the message in the “plain” line and writes down the corresponding letter in the “cipher” line.

> **Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG**

> **Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD**

Deciphering is done in reverse, with a right shift of 3.

Your challenge consists of writing 2 modules:

1. `encrypt.py`, which takes two inputs (a plain text and a key) and returns the ciphertext corresponding to the given plain text.

2. `decrypt.py`, that takes two inputs (a ciphertext and a key) and returns the plain text corresponding to the given ciphertext.