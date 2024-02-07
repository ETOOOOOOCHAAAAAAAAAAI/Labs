def permutations(string):
    if len(string) <= 1:
        return [string]
    else:
        perms = []
        for perm in permutations(string[1:]):
            for i in range(len(perm) + 1):
                perms.append(perm[:i] + string[0] + perm[i:])
        return perms

user_input = input()
print(permutations(user_input))
