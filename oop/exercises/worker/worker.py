from abc import ABC, abstractmethod
from tool import Laptop


# Complete the class Worker
class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        print(f"\n\n{self.name} starts working:")

    @abstractmethod
    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")


# Complete this class, so that it would work properly. Implement the missing methods
class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        print("The programmer is coding")

    def take_break(self, minutes):
        print(f"\n\n{self.name} takes {minutes} minutes break:")

programmer_1 = Programmer('Michael', 'Python')

programmer_1.work()
programmer_1.take_break(15)
print(programmer_1)


# Complete the class Janitor.
# Janitor is a subclass of the class Worker
# work(): Janitor fixes pipes with "tool"
# take_break(): Janitor listens to music

class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def work(self):
        print(f'\n\n{self.name} fixes pipes with {self.tool}.')


    def take_break(self, minutes):
        self.minutes = minutes      
        print(f'{self.name} listens to music {self.minutes} minutes.')


    def __str__(self):
        return f"{self.name} uses {self.tool}"
    

janitor_1 = Janitor('Taylor', 'Wrench')


janitor_1.work()
janitor_1.take_break(20)
print(janitor_1)



