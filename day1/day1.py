import sys

ans = 0
cur_ans = 0
answers = {}

l = list(sys.stdin)

while True:
    for line in l:
        line = line.strip()
        cur_ans += int(line)
        answers[ans] = 1
        if cur_ans in answers:
            print(cur_ans)
            sys.exit() 
        ans =  cur_ans