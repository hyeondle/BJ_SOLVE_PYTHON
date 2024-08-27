import sys
import math
d = sys.stdin.read().splitlines()

n, k = map(int, d[0].split())
m, f = [], []
for i in range(n) :
    s, g = map(int, d[i+1].split())
    if s == 1 :
        m.append(g)
    else :
        f.append(g)
count = 0

ml = []
fl = []
for i in range(6) :
    count += math.ceil(m.count(i + 1) / k) + math.ceil(f.count(i + 1) / k)
    
print(count)