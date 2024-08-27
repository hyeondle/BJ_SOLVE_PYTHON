def custom_round(value):
    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)

import sys
n = int(input())
if n == 0 :
    print("0")
    exit()
data = list(map(int, sys.stdin.read().splitlines()))

k = custom_round(n / 100 * 15)
data.sort()

data = data[k:n-k:]
print(custom_round(sum(data)/(n-2*k)))