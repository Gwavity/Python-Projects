import itertools
import string

with open("2chars.txt","w") as char:
    charCombo = itertools.product(string.ascii_lowercase, repeat=4)
    chars = ["".join(i) + "\n" for i in charCombo]
    char.writelines(chars)
