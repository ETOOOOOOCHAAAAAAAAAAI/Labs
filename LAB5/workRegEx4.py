import re


def find_A_with_a(string):
    return re.findall("[A-Z][a-z]+", string)


print(find_A_with_a("AaaBbbCcc"))