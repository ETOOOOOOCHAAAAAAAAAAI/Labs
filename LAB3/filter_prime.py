numbers = input().split()
numbers = [int(num) for num in numbers]

def is_prime(numbers):
    for num in numbers:
        x = 0
        if num == 1:
            continue
        for k in range(1, num + 1):
            if num % k == 0:
                x += 1
        if x <= 2:
            print(num)


is_prime(numbers)