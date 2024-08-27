import sys

data = sys.stdin.read().splitlines()
x = int(data[0])
time = list(map(int, data[1].split()))

time.sort()
sum = 0
res = 0
for t in time :
    sum += t
    res += sum
print(res)

