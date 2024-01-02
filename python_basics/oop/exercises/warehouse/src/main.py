############################
# You can test your code with this example code
# No need to modify this file
############################

from funcs import add_employees, get_employees_numbers
from warehouse import Warehouse


if __name__ == "__main__":
    while True:
        print("\n###########\nChoose action:")
        print("1 - Show warehouse Status")
        print("2 - Add Employees to warehouse")
        print("0 - Quit")
        choice = int(input("Choose option: "))
        print(">>>")
        if choice == 1:
            print(Warehouse())
            d, p = get_employees_numbers()
            print(f"Delivery-men: {d}, Packagers: {p}")
        elif choice == 2:
            add_employees()
        elif choice == 0:
            print("Good bye!")
            break
        else:
            print("Invalid input")

