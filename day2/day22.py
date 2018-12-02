import sys

l = list(sys.stdin)

words = []
for line1 in l:
    for line2 in l:
        line1 = line1.strip()
        line2 = line2.strip()

        count = 0
        letters = []
        for i in range(len(line1)):
            if line1[i] == line2[i]:
                count += 1
                letters.append(line1[i])

        if count == len(line1) - 1:
            print(''.join(letters))

