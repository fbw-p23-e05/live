import colors

def print_rectangle_properties(rectangle):
    print(
        colors.ANSI_PURPLE + "Printing properties of Rectangle:" + colors.ANSI_RESET
    )

    # width
    print(
        colors.ANSI_CYAN
        + "Width"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_width())
        + colors.ANSI_RESET
    )

    # height
    print(
        colors.ANSI_CYAN
        + "Height"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_height())
        + colors.ANSI_RESET
    )

    # area
    print(
        colors.ANSI_CYAN
        + "Area"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_area())
        + colors.ANSI_RESET
    )

    # perimeter
    print(
        colors.ANSI_CYAN
        + "Perimeter"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_perimeter())
        + colors.ANSI_RESET
    )

    # diagonal
    print(
        colors.ANSI_CYAN
        + "Diagonal"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_diagonal())
        + colors.ANSI_RESET
    )

    print(
        colors.ANSI_BLACK + "==================================" + colors.ANSI_RESET
    )

import math
# from check import print_rectangle_properties


class Rectangle:

    def __init__(self, width: float, height: float) -> None:
    # def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return math.sqrt((self.width**2) + (self.height**2))
    
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    

def main():
    rectangle1 = Rectangle(2.0, 8.0)
    print_rectangle_properties(rectangle1)

    rectangle2 = Rectangle(2.0, 8.0)
    print_rectangle_properties(rectangle2)

if __name__ == "__main__":
    main()