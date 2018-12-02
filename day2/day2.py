import sys
from collections import Counter
l = list(sys.stdin)

twos = 0
threes = 0
for line in l:
    line = line.strip()
    counts = {}
    for letter in line:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    foundTwo = False
    foundThree = False
    vals = []
    for key, val in counts.items():
        vals.append(val)
    vals = set(vals)

    print(vals)

    if 3 in vals:
        threes += 1
    if 2 in vals:
        twos += 1

print(twos, threes)
print(twos * threes)
