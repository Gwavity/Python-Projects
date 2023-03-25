import itertools
import string

with open("2chars.txt","w") as char:
    charCombo = itertools.product(string.ascii_lowercase, repeat=4)
    chars = []
    for i in charCombo:
        chars.append("".join(i) + "\n")
    char.writelines(chars)
