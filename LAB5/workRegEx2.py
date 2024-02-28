import re


def finda_and_2_or_b(string):
    return re.fullmatch("ab{2,3}", string) is not None


print(finda_and_2_or_b("abbbb"))
print(finda_and_2_or_b("abb"))