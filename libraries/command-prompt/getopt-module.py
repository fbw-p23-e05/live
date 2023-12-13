import getopt
import sys 

first_name = None
last_name = None

# get list of arguments
argv = sys.argv[1:]
print(argv)

# Pass the the list of arguments
# enumerate according to the created flag/option
opts, args = getopt.getopt(argv, "f:l:a:")
print(opts)

# Loop over the lost of options
# Enumerate the tuples of options and arguments
for opt, arg in opts:
    if opt == "-f":
        first_name = arg
        print(first_name)
    elif opt == "-l":
        last_name = arg
        print(last_name)
