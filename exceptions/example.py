class Animal:
    
    def __init__(self, animal_name):
        print(animal_name, "is a nice animal")
        
        
class Dog(Animal):
    
    def __init__(self):
        print("Dogs can bark")
        super().__init__('Dog')
        
        
animal = Animal("Parrot")
print(animal)

dog_1 = Dog()
print(dog_1)
        
        