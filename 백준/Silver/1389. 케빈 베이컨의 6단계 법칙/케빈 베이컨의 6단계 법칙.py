import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())

INF = 1000000000

tab = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    tab[i][i] = 0

for x in range(m):
    a, b = map(int, data[x + 1].split())
    tab[a][b] = 1
    tab[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tab[i][j] > tab[i][k] + tab[k][j]:
                tab[i][j] = tab[i][k] + tab[k][j]

min_bacon = INF
min_person = -1

for i in range(1, n + 1):
    bacon_sum = sum(tab[i][1:])
    if bacon_sum < min_bacon:
        min_bacon = bacon_sum
        min_person = i

print(min_person)