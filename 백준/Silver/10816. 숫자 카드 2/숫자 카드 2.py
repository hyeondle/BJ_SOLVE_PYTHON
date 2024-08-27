import sys

data = sys.stdin.read().splitlines()

lis = [0] * 20000001
s_h = list(map(int, data[1].split()))
n = int(data[0])
for _ in range(n) :
    lis[s_h[_]+10000000] += 1
k = int(data[2])
s_c = list(map(int, data[3].split()))
for _ in range(k) :
    print(lis[s_c[_] +10000000], end=' ')
    
    