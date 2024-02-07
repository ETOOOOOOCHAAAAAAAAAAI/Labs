numbers = input().split()
numbers = [int(num) for num in numbers]

def unique_elements(numbers):
    numbers1 = []
    for i in range(len(numbers)):
        if numbers[i]  not in numbers1:
            numbers1.append(numbers[i])
    print(numbers1)


unique_elements(numbers)