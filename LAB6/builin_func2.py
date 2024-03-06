def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count


s = "Hello, World!"
upper_count, lower_count = count_case(s)
print(f"Количество заглавных букв: {upper_count}")
print(f"Количество маленьких букв: {lower_count}")
