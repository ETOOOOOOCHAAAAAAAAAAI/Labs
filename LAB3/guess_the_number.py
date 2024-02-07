import random

def guess_numbers():
    text1 = input("Hello! What is your name?""\n")
    print("Well,",text1,",I am thinking of a number between 1 and 20.")
    random_numb = random.randint(1, 20)
    i = 1
    while True:
        s = int(input("Take a guess.""\n"))
        if s == random_numb:
            print("Good job,",text1,"!You guessed my number in", i, "guesses!")
            break
        else:
            print("Your guess is too low.")
            i += 1
            continue

guess_numbers()
