import re


def replace_by_AaA(string):
        return re.sub('_([a-z])', lambda m: m.group(1).upper(), string)


print(replace_by_AaA("aaaa_aaaa_bbbb"))