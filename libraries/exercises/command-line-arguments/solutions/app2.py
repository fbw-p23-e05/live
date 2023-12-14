import sys
import getopt

try:
    args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])[0]

    name = None

    for arg in args:
        if arg[0] in ['-h', '--help']:
            print("This program allows you to say Good Morning.\n\n"
                  "-n/--name <name> - prints out a good morning message.")
        # if arg[0] in ['-n', '--name']:
        #     name = arg[1]
        if ('n' or '--name') in arg[0]:
            name = arg[1]

    if name:
        print(f"Good Morning {name}")
    else:
        print("Good Morning Folks")
except getopt.GetoptError:
    print("Good Morning Folks")
