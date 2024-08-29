import sys
from math import comb

n = int(sys.stdin.read().strip())
result = 0

for r in range(n // 2 + 1):
    result += comb(n - r, r)
    result %= 10007

print(result)