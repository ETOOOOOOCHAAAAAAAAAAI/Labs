def spy_game(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 0 and numbers[i + 1] == 0 and numbers[i + 2] == 7:
            print("True")
            break
        elif i == len(numbers) - 1:
            print("False")
            break


spy_game([1,2,3,4,5,6,7])
