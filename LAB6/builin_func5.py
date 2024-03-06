def check_all_true(t):
    return all(t)


my_tuple = (True, 1, "hello")
print(check_all_true(my_tuple))
my_tuple = (True, 0, "hello")
print(check_all_true(my_tuple))
