import os


def delete_file_if_exists(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        return f"Файл '{file_path}' успешно удален."
    elif not os.path.exists(file_path):
        return f"Файл '{file_path}' не существует."
    else:
        return f"Нет доступа для удаления файла '{file_path}'."


file_path = "C:/Users/ASUS TUF Gaming F15/Desktop/PP2LAB/LAB6/E.txt"
result = delete_file_if_exists(file_path)

