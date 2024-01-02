from animal import Animal

from dog import Dog


class GermanShepard(Dog):

    # TODO: override the walk() method

    def walk(self):
        super().walk()
        print("German Shepard`s show their beautiful color while running.")

