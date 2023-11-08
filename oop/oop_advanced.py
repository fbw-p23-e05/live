

# class Vehicle:

#     def move(self):
#         raise NotImplementedError('Abstract method is not implemented yet.')


# train = Vehicle()

# print(train.move())





from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    def fuel(self):
        return 'Refuel the vehicle every 3 days.'


class Car(Vehicle):

    def move(self):
        return 'Car is moving.'
    
    def stop(self):
        return 'Car has stopped.'
    

class Bike(Vehicle):

    def move(self):
        return 'Bike is moving.'
    
    def stop(self):
        return 'Bike has stopped.'
    
car_1 = Car()
bike_1 = Bike()


# print(car_1.move())
# print(car_1.stop())
# print(car_1.fuel())

# print(bike_1.move())
# print(bike_1.stop())
# print(bike_1.fuel())


# print(Bike.mro())
# print(Bike.__mro__)
# print(dir(bike_1))


class FlyingAbilityMixin:

    def fly(self):
        return 'This vehicle can fly.'
    

class SubmarineAbilityMixin:

    def dive(self):
        return 'This vehicle can dive underwater.'



class FlyingCar(Car, FlyingAbilityMixin):

    pass


class SubmarineBike(Bike, SubmarineAbilityMixin):

    pass


car_copter = FlyingCar()
bike_marine = SubmarineBike()

# print(car_copter.move())
# print(car_copter.fly())

# print(bike_marine.stop())
# print(bike_marine.dive())


# print(SubmarineBike.mro())




# Overloading




class Calculator:

    # def number_sum(self, a, b):

    #     self.a = a
    #     self.b = b

    #     total = self.a + self.b

    #     return total

    def number_sum(self, a, b, c=0):

        self.a = a
        self.b = b
        self.c = c

        total = self.a + self.b + self.c
        # total = a + b + c

        return total
    
    def number_multiply(self, x, y=1, z=1):

        self.x = x
        self.y = y
        self.z = z

        product = self.x * self.y * self.z
        # product = x * y * z

        return product

    
add_two = Calculator()

# print(add_two.number_sum(10, 20, 3))
# print(add_two.number_multiply(10))



# Overriding


class MobileTech:

    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_type(self):
        print('This phone has IPS display.')



class Smartphone(MobileTech):

    def __init__(self, brand, ram, storage, model, camera):
        super().__init__(brand, ram, storage)
        self.model = model
        self.camera = camera
        super().display_type()

    
    def display_type(self):
        # super().display_type()
        print('This phone has Amoled display.')


phone_1 = MobileTech('Samsung', 8, 256)
phone_2 = Smartphone('Apple', 6, 128, 'iPhone X', '12MP')

# print(phone_1.brand)
# print(phone_1.model)

print(phone_1.display_type())
print(phone_2.display_type())







