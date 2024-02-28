import re


def find_with__(string):
    return re.findall("[a-z]+_[a-z]", string)


print(find_with__("aaaa_aaaa_bbbb_ccccc"))