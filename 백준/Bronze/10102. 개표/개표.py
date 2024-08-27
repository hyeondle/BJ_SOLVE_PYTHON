import sys
data = sys.stdin.read().splitlines()

a = b = 0
for _ in data[1] :
    if _ == 'A' :
        a += 1
    else :
        b += 1
if a == b :
    print('Tie')
elif a> b :
    print('A')
else :
    print('B')