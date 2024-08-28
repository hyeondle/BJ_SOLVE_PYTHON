import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
nums = list(map(int, data[1].split()))

presum = [0] * (n + 1)
for i in range(1, n + 1):
    presum[i] = presum[i - 1] + nums[i - 1]

for k in range(m):
    i, j = map(int, data[k + 2].split())
    print(presum[j] - presum[i - 1])