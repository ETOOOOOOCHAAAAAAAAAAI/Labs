import os

def test_path(path):
    if os.path.exists(path):
        print(f"Указанный путь '{path}' существует.")
        if os.path.isfile(path):
            print(f"Имя файла: {os.path.basename(path)}")
        if os.path.isdir(path):
            print("Путь указывает на директорию.")
        print(f"Директория: {os.path.dirname(path)}")
    else:
        print(f"Указанный путь '{path}' не существует.")


path_to_check = "C:/Users/ASUS TUF Gaming F15/Desktop/PP2LAB"
test_path(path_to_check)
