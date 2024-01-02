###########################
# Do not modify this file
###########################
import random
from password_generator_factory import PasswordGeneratorFactory


if __name__ == "__main__":
    while True:
        print("\n###########\nChoose action:")
        print("1 - Use Alpha Generator")
        print("2 - Use Alpha-Numerical Generator")
        print("0 - Quit")
        choice = int(input("Choose option: "))
        print(">>>")
        if choice == 1:
            ag = PasswordGeneratorFactory.create_object("Alpha")
            print("Generating 5 passwords samples")
            for i in range(5):
                print(ag.generate_password(random.randint(6, 10)))
        elif choice == 2:
            ang = PasswordGeneratorFactory.create_object("AlphaNumeric")
            print("Generating 5 passwords samples")
            for i in range(5):
                print(ang.generate_password(random.randint(6, 10)))
        elif choice == 0:
            print("Good bye!")
            break
        else:
            print("Invalid input")

