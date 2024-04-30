my_list = ['Apple', 'Banana', 'Cherry', ]
with open('my_file1.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print('Список успешно записан в файл.')
