# (¬x ∨ ¬y) ∧ ¬(x ≡ z) ∧ w.
print("x | y | z | w | r")
from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    r = (not x or not y) and not (x == z) and w
    if r:
        print("--+---+---+---+--")
        print(x, y, z, w, r, sep = " | ")