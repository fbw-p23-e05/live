import sys 
import os 

if len(sys.argv) < 3:
    print("Usage: python3 rename_files.py <prefix> <file1> <file2> ..... ")
    sys.exit(1)
    
else:
    prefix = sys.argv[1]
    
    for file in sys.argv[2:]:
        if os.path.isfile(file):
            new_filename = prefix + file
            os.rename(file, new_filename)
        else:
            print("File does not exist.")
            