import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
nums = list(map(int, data[1].split()))
v = int(data[2])
count = nums.count(v)

print(count)
    