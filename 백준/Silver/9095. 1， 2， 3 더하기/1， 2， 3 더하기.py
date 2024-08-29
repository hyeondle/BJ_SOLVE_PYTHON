import sys

data = sys.stdin.read().splitlines()

n = int(data[0])

for i in range(n) :
    k = int(data[i+1])
    dp = [0] * max((k + 1), 4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if k < 4 :
        print(dp[k])
        continue
    for x in range(4, k+1) :
        dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
    print(dp[k])