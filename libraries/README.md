# Libraries

- Modules
- Imports
- pip
- Virtual Environment

## Modules

- Module is a file that contains code to perform as specific task.
- May contain: variables, functions, classes, etc.
- Allows to separate and organize our code as our applications get bigger.

## Virtual Environments

> The enviroment is created in you current working directory

1. Create the virtual environment
    ```
    # Linux
    python3 -m venv <environment_name>

    # Windows 
    python -m venv <environment_name>
    ```

2. Activate the virtual environment
    ```
    # Linux
    source <environment_name>/bin/activate

    # Windows
    <environment_name>\Scripts\activate
    ```

3. Install/download a package

    ```
    pip install <package name>
    ```

4. Check installed pckages

    ```
    pip list
    pip freeze
    ```

5. Create a requirements file

    ```
    pip freeze > <filename>
    ```

6. Deactivate virtual environment

    ```
    deactivate
    ```

7. Install packages from a requirements file

    ```
    pip install -r <filename>
    ```
