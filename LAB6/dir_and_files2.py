import os


def check_path_access(path):
    exists = os.path.exists(path)
    print(f"Путь существует: {exists}")

    readable = os.access(path, os.R_OK)
    print(f"Путь доступен для чтения: {readable}")

    writable = os.access(path, os.W_OK)
    print(f"Путь доступен для записи: {writable}")

    executable = os.access(path, os.X_OK)
    print(f"Путь доступен для выполнения: {executable}")


path_t_c = "C:/Users/ASUS TUF Gaming F15/Desktop/PP2LAB"
check_path_access(path_t_c)
