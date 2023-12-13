## Command Line arguments

- `sys.argv`
- getopt module
- argparse module

1. Options - modify the bahaviour of a particular command or program.
2. Arguments - represent the source or destination to be processed.
3. Subcommands - allow a program to define more than one command with the respective set of options and arguments.

## Sys Module

- Built-in Python Module
- Provides access to system-related functionalities and information.
- useful for:
    1. Accessing cmd arguments -Allows you to access command line arguments passed to the script via the `sys.argv` attribute. 
    2. Managing Python runtime environment - Provides insights into the Python interpreter and its environment - version number, platform, and byte order.
    3. Handling standard input, output and error streams -  offers access to standard input (`sys.stdin`), standard output (`sys.stdout`) and error streams (`sys.stderr`). 
    4. Manipulating the module search path. - The `sys.path` attribute allows you to modify the module search path at runtime, allowing you to import modules from custom locations or to control order of importation.

1. Structure of `sys.argv`:
    ```
    python3 script.py arg1 arg2 arg3 arg4

    # Result
    ['script.py', 'arg1', 'arg2', 'arg3', 'arg4']
    ```

## `getopt` module

1. args - represents the type of arguments to be pass through.
2. options - the string of option letter that the script wants to recognize.

