# numbers = input().split()
# numbers = [int(num) for num in numbers]
#
#
# def has_33(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] == 3 and numbers[i + 1] == 3:
#             print("True")
#             break
#         elif i == len(numbers) - 1:
#             print("False")
#             break
#
#
# has_33(numbers)

def has_33(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            print("True")
            break
        elif i == len(numbers) - 1:
            print("False")
            break


has_33([1, 3, 3])
