numheads = int(input())
numlegs = int(input())

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            print("курицы:",num_chickens, "кролики:",num_rabbits)

solve(numheads, numlegs)

