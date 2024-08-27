import sys
n, m = map(int,input().split())
names = sys.stdin.read().splitlines()
no_h = set()
no_l = set()

for _ in range(n) :
    no_h.add(names[_])
for _ in range(m) :
    no_l.add(names[_+n])
print(len(no_h.intersection(no_l)))
print('\n'.join(sorted(no_h.intersection(no_l))))