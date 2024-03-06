import os


def list_directories_files(path):
    print(f"all directories and files in {path}:")
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            print(f"Directory: {f}")
        elif os.path.isfile(os.path.join(path, f)):
            print(f"File: {f}")


def list_only_directories(path):
    print(f"only directories in {path}:")
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            print(f"Directory: {f}")


def list_only_files(path):
    print(f"only files in {path}:")
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            print(f"File: {f}")


my_path = "C:/Users/ASUS TUF Gaming F15/Desktop/PP2LAB"


list_only_directories(my_path)
list_only_files(my_path)
list_directories_files(my_path)


