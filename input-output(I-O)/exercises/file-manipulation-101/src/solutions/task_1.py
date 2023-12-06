"""List contents of a directory"""
import os

def show_data_list():
    """Print the contents of the directory."""
    files_list = sorted(os.listdir("../data/initial"))
    
    for file in files_list:
        print(file)
show_data_list()

# import os


# file = os.path.join(os.path.join("../data/initial"))

# if os.path.isdir(file):
#         contents = os.listdir(file)
#         print(f"Contents of directory '{file}':")
#         for item in contents:
#             print(item)