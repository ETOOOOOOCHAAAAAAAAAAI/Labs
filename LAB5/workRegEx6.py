import re


def replace(string):
    return re.sub("[,.]", ":", string)


print(replace("a.a.a.a..,b,b,b,b,b,b,b,b,"))