import sys

data = sys.stdin.read().splitlines()

d_l = list(map(int, data[1].split()))

print(min(d_l), end=' ')
print(max(d_l))
