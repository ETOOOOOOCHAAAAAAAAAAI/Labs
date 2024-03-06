import os

def count_lines(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    else:
        return "Файл не найден или не является файлом."


file_path = "C:/Users/ASUS TUF Gaming F15/Desktop/PP2LAB"
line_count = count_lines(file_path)
print(line_count)
