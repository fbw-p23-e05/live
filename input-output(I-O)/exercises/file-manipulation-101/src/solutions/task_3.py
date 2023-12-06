"""Create directories for a list."""
import os

ROOT = os.getcwd()
DATA_ROOT = os.path.join(ROOT, 'src/data/initial')


def create_data_directories(dir_list):
    for dir in dir_list:
        try:
            os.mkdir(f"{DATA_ROOT}/{dir}")
        except FileExistsError:
            print(f"The directory {dir} already exists.")
 
        
dirs = ["personal", "work"]
create_data_directories(dirs)
