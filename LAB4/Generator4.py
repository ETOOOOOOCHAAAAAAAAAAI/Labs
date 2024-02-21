def Square(a, b):
    for i in range(a, b):
        yield i ** 2

for i in Square(1, 11):
    print(i)