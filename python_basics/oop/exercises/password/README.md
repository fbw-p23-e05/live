[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/gRBmbOxf)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12829932&assignment_repo_type=AssignmentRepo)
# Factory method
Consider the following class diagram:
![class diagram](class_diagram.PNG)


**PasswordGenerator**: abstract class that represents password generators

**AlphaGenerator**: subclass of *PasswordGenerator*. Represents password generators based on letters only.

**AlphaNumericGenerator**: subclass of *PasswordGenerator*. Represents password generators based on letters and numbers.

**PasswordGeneratorFactory**: A factory class for creating *PasswordGenerator* objects.

> At any time, run the file **src/main.py** to get an interactive menu to check if your code is behaving properly. 

## Task
- [ ] In the file *src/password_generator_factory.py*, complete the method **create_object(generator_type)** in the class **PasswordGeneratorFactory** so that:
* If the parameter generator_type is equal to `"Alpha"`, create an instance of **AlphaGenerator**
* If the parameter generator_type is equal to `"AlphaNumeric"`, create an instance of **AlphaNumericGenerator**
* Do not forget to process invalid arguments

> Note that the **create_object(generator_type)** is a static method.

To test your code, run the command:
```
python src/check.py
```
