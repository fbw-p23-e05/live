# Python-testing-pytest

In this exercise, you will be using [pytest](https://pytest.org) for testing. Add the `squared()`
function in `src/app.py`. Then create the tests inside of `src/test_app.py` so that they do what
their name explains they do. Run *pytest* by executing `pytest` inside the `src/` directory.

# Exceptions
An exception in python is an event that occurs during the execution of programs that disrupts the normal flow of execution.

Exceptions are object and contain:
- Error type (exception name)
- An error message describing the error event

An exception can be raised with the `raise` keyword:
```
 def print_list(str_list: list) -> None:
    if type(str_list) != list:
      raise TypeError("wrong type")
```

To test if `print_list` raises a TypeError if an argument of the wrong type is passed, you can use `pytest.raises(TypeError)`. pytest.raise is a context manager and to use it you have to use the *with* statement. 

The Python *with* statement creates a runtime context that allows you to run a group of statements under the control of a context manager. 

For example:
```
def test_print_list():
  with pytest.raises(TypeError):
    print_list(1)
