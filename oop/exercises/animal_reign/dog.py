from animal import Animal

class Dog(Animal):

    #TODO create a constructor for Dog, with 4 legs and 2 eyes!

    def __init__(self):
        super().__init__(4, 2)


    #TODO override the breathe() method!

    def breathe(self):
        super().breathe()
        print('Dogs love to breathe with their mouths open.')


    #TODO override the walk() method!


    def walk(self):
        super().walk()
        print('Dogs love to run.')