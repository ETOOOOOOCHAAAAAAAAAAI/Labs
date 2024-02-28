import re


def insert_spaces(string):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", string)


print(insert_spaces("SpaceHereAndHere"))