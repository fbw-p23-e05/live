"""
Iterate and print the lines of a file.
"""


def print_line(line):
    """
    Print a line without the line break.
    """
    print(line.replace("\n", ""))


with open('../data/task3.txt') as file:
    # store the even lines
    even_lines = []
    
    for num, line in enumerate(file):
        if (num + 1) % 2 == 0:
            even_lines.append(line)
        else:
            print_line(line)

    # loop over and print the even lines
    for line in even_lines:
        print_line(line)
