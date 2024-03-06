def is_palindrome(s):
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]


s = "А роза упала на лапу Азора"
print(is_palindrome(s))
