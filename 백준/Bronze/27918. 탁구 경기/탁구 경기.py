import sys

d = sys.stdin.read().splitlines()

n = int(d[0])
dalgu, phonix = 0, 0
for i in range(n) :
    c = d[i+1]
    if c == 'D' :
        dalgu += 1
    else :
        phonix += 1
    if abs(dalgu - phonix) >= 2 :
        break

res = str(dalgu) + ':' + str(phonix)
print(res)