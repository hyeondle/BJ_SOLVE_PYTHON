import sys
data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
rt = list(range(1, n + 1))

for _ in range(m):
    i, j, k = map(int, data[_ + 1].split())
    i -= 1
    j -= 1
    k -= 1

    p = rt[k:j+1]
    a = rt[i:k]
    rt[i:j+1] = p + a

print(" ".join(map(str, rt)))