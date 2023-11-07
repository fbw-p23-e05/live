
## Today - 2023.11.07

* Different types of method: 

- instance method

- class method

- static method

* Using getters and setters

* Exercises


### Instance method

* Instance methods are functions within a class that operate on individual instances or objects. 

* They can access and modify the object's attributes.


### Class method

* Class methods belong to the class and are accessible to all instances. 

* They manipulate or provide functionalities related to the entire class, rather than individual objects.

* They take 'cls' as the first argument, allowing access to class-level variables and operations.


### Static method

*  Static methods are independent of class and instance variables.

* They operate like regular functions, residing within the class for organization purposes.

* They don’t take 'self' or 'cls' arguments and don’t access or modify class or instance-specific data.

### Getter and Setter

#### Getter
* Getters are methods used to retrieve the value of a private attribute.

* They provide read access to the attribute.

* They allow controlled access to private attributes, enabling encapsulation, and can include validation or processing before returning the attribute's value.


#### Setter
* Setters are methods used to change or set the value of a private attribute.

* They provide write access to the attribute.

* They offer controlled modification to ensure encapsulation and can include validation or processing before setting the attribute's value.

