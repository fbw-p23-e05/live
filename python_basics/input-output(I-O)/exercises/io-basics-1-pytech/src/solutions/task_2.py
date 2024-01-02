"""Count the lines of task2.txt"""

with open("../data/task2.txt") as file:
    print(len(list(file)) - 2)
