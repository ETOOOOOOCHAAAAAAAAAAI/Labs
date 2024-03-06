for letter in range(65, 91):
    file_name = f"{chr(letter)}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is the file for letter {chr(letter)}.\n")

print("Файлы успешно созданы.")
