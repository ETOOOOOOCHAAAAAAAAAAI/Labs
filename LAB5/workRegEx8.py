import re


def split_all_upper(string):
    return re.findall('[A-Z][^A-Z]*', string)


print(split_all_upper("splitHereAndHere"))