import os


# def rm(filename):
#     os.remove(filename)
    
def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        raise FileNotFoundError('The file is not found.')


# rm('somefile1.txt')