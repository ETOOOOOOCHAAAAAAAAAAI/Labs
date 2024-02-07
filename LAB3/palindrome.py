s = input()

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

is_palindrome(s)