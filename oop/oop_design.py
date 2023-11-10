

class Person:

    _instance = None

    def __new__(cls, name, age):
    
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def shopping(self):
        pass

  
# person_1 = Person('Mathews', 27)
# print(person_1.name)

# person_2 = Person('Harris', 30)
# print(person_2.name)

# person_3 = Person('Emily', 22)
# print(person_3.name)

# # print(person_1 is person_2)
# # print(person_2)


# print(person_1.name)
# print(person_2.name)

# print(person_1)
# print(person_2)
# print(person_3)



def singleton(cls):

    instance = {}

    def inner(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    
    return inner


@singleton
class Singleton:
    def __init__(self, name):
        self.name = name

# s1 = Singleton('Mathews')
# s2 = Singleton('Harris')
# s3 = Singleton('Emily')

# # print(id(s1))
# # print(id(s2))
# # print(id(s3))

# print(s1.name)
# print(s2.name)
# print(s3.name)

# print(s1 is s2)


# Factory design pattern


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):

    def move(self):
        return 'Car is moving.'
    

class Bike(Vehicle):

    def move(self):
        return 'Bike is moving.' 
    

class Train(Vehicle):

    def move(self):
        return 'Train is moving.'  
    

class Aeroplane(Vehicle):

    def move(self):
        return 'Aeroplane is flying.'  


class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass

    # @staticmethod
    # def start_factory(type):

    #     factory_type = {'car': Car(), 'bike': Bike(), 'train': Train()}

    #     return factory_type[type]

class CarFactory(VehicleFactory):

    def create_vehicle(self, type):
        self.type = type
        return start_factory(self.type)
    

# class BikeFactory(VehicleFactory):

#     def create_vehicle(self):
#         return Bike()

class BikeFactory(VehicleFactory):

    def create_vehicle(self, type):
        self.type = type
        return start_factory(self.type)


class AeroplaneFactory(VehicleFactory):

    def create_vehicle(self, type):
        self.type = type
        return start_factory(self.type)

# def start_factory(type):

#     if type == 'car':
#         return Car()
#     elif type == 'bike':
#         return Bike()
#     elif type == 'train':
#         return Train()


def start_factory(type):

    factory_type = {'car': Car(), 'bike': Bike(), 'train': Train(), 'aeroplane': Aeroplane()}

    return factory_type[type]


car_factory_1 = CarFactory()
bike_factory_1 = BikeFactory()

print(car_factory_1.create_vehicle('car').move())
print(bike_factory_1.create_vehicle('bike').move())


# Create a truck object and call any method from that object using factory design pattern.
