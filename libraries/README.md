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

## Creating and uploading packages to PyPI

1. Create the directory structure

2. Add `__init__.py` file to the modules and submodules

3. Once the code is ready import the files and functions/methods to the `__init__.py` file of that respective directory.

4. Add setup file to the base directory:
    ```python
    from setuptools import setup, find_packages

    VERSION = "0.0.1"
    DESCRIPTION = "The first package for PyTech"
    LONG_DESCRIPTION = "We are embarking on a journey to create our very first simple python package."

    setup(
        # name must match the simple_calculator folder name
        name="simple_calculator",
        version=VERSION,
        author="<Your Name>",
        author_email="<Your Email>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],  # any additional packages used in our code
        # Installed alongside your package.
        
        keywords=['python', 'calculator', 'math',],
        classifiers=[
            "Development Status :: Beta",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Linux :: Ubuntu",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
    )
    ```

5. Add licence text to `LICENSE` file.
    > https://choosealicense.com/

6. Build the packages needed for upload:

    ```shell
    python3 setup.py sdist bdist_wheel
    ```

7. Check if `twine` is installed
    ```
    pip show twine
    ```

8. Install `twine` package
    ```
    pip install twine
    ```

9. Use `twine` to upload to PyPI

    ```shell
    twine upload dist/*
    ```
    > Ensure that you have enabled 2FA(Two Factor Authentication)
    > Generate API tokens for use on uploads.
    > When prompted: username: `__token__`, password: `<Generated API Token>`


