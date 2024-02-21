def square(N):
    for i in range(N):
        yield i ** 2

for i in square(10):
    print(i)