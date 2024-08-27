n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)

count = 0
for coin in data:
    if coin <= k:
        count += k // coin
        k %= coin
    if k == 0:
        break

print(count)