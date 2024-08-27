import sys
data = sys.stdin.read().splitlines()

a = set(map(int, data[1].split()))
count = int(data[2])
hex = list(map(int, data[3].split()))
r = []
for _ in range(count) :
    if hex[_] in a :
        r.append(1)
    else :
        r.append(0)
print('\n'.join(map(str,r))+'\n')