def reverse_sentence(s):
    w = s.split()
    rw = reversed(w)
    rs = ' '.join(rw)
    return rs

user_input = input()
reversed_sentence = reverse_sentence(user_input)
print(reversed_sentence)
