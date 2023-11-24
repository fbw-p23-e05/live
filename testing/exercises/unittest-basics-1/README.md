# Unittest basic 1


## Task1

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will return the `"ABCDEF"` when called with the argument "abcdef".

## Task2

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `True` when called with the argument `['I', 'LOVE', 'YOU']`.

## Task3

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `False` when called with the argument `['i', 'LOVE', 'YOU']`.

# assertRaises

For the following tasks, you need to use `assertRaises`. Python unittest `assertRaises` allows you to verify that a certain exception is raised when your code is run. To use `assertRaises` a context manager is needed.

Example of the usage of a context manager:

```
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```
Context managers are able to check for specific types of exceptions and prevent them from being raised. This comes in handy when checking for raised exceptions during testing.

For example:
The following test 
```
def test_assert_raises(self)
    with self.assertRaises(KeyError):
        raise KeyError
```
would pass.

On the other hand
```
def test_assert_raises(self)
    with self.assertRaises(KeyError):
        raise IndexError
```
would fail.    


## Task4

Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a string (**str**).

## Task5

Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a **list**.

## Task6

Fix both functions **to_upper** and **to_word_list_isupper** in `src/text.py` so they will raise a **TypeError** if the argument was not the right type (**string** in the case of `to_upper` and **list** in the case of `to_word_list_upper`).


## Objectives:
- Learn about assertEqual.
- Learn about assertTrue.
- Learn about assertFalse.
- Learn about assertRaises.

> **Hint:** Run the tests by executing:

    python3 test.py

> Or run the test with more details by executing:

    python3 -m unittest -v test.py
