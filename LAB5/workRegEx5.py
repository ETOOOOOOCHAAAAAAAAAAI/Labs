import re


def a_anything_b(string):
    return re.fullmatch("a.*b", string) is not None


print(a_anything_b("afkffkjfkgjfkb"))
print(a_anything_b("aaaaaabbbbb"))