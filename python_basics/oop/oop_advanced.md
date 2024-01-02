




## Today - 2023.11.08

* Abstract Classes and methods

* Mixins

* Overloading and Overriding

* Exercises



### Abstract Classes and Methods:

* Abstract classes serve as templates or blueprints for other classes. 

* They cannot be instantiated on their own, and they may contain abstract methods or even concrete methods.

* Abstract methods within an abstract class are methods without an implementation.

* They serve as placeholders, requiring subclasses to implement these methods, ensuring the necessary behaviors are defined.

* Python does not provide abstract classes by default. It comes with a module 'ABC' that provides the base for defining Abstract Base classes(ABC).


### Method Resolution Order (MRO)

* Method Resolution Order refers to the order in which Python searches for and executes methods in classes that involve inheritance.

* Python uses the C3 Linearization algorithm to construct a consistent linearization.

* MRO ensures that the inheritance hierarchy is respected, allowing methods to be resolved in a predictable and consistent order, avoiding ambiguity in multiple inheritance situations.


### Mixins
* Mixins are supplementary classes used to provide additional functionalities to other classes without being independent entities.

* They are designed to be mixed into various classes to extend their functionalities.

### Overloading

* Overloading allows defining multiple methods within the same class, but with different parameters or varying numbers of arguments.

* Python does not support method overloading by default since two methods cannot have the same name in Python.

* In Python, we can overload methods by defining it in such a way that there exists more than one way to call it.

### Overriding

* Overriding occurs in inheritance when a subclass redefines a method that's already present in its superclass.

* The redefined method in the subclass can provide a modified or completely new implementation, altering the inherited method's behavior.

