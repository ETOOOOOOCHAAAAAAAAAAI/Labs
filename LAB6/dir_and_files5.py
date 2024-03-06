my_list = ['Apple', 'Banana', 'Cherry', 'Date']
with open('my_file.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print('Список успешно записан в файл.')
