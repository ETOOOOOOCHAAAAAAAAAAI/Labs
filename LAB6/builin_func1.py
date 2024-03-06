def multiply_in_list(numbers):
    if not numbers:
        return None
    result = 1
    for number in numbers:
        result *= number
    return result


listnumb = [1, 2, 3, 4, 5]
result = multiply_in_list(listnumb)
print(result)
