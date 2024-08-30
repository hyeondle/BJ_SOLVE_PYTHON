import sys
from collections import deque

data = sys.stdin.read().splitlines()

n, m, v = map(int, data[0].split())

g = [[] for _ in range(n + 1)]

for i in range(m):
    k, x = map(int, data[i + 1].split())
    g[k].append(x)
    g[x].append(k)

for i in range(1, n + 1):
    g[i].sort()

def dfs(v, visit, res):
    visit[v] = True
    res.append(v)
    for i in g[v]:
        if not visit[i]:
            dfs(i, visit, res)

def bfs(v, visit, res):
    queue = deque([v])
    visit[v] = True
    while queue:
        x = queue.popleft()
        res.append(x)
        for i in g[x]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

visit = [False] * (n + 1)
res_dfs = []
dfs(v, visit, res_dfs)
print(' '.join(map(str, res_dfs)))

visit = [False] * (n + 1)
res_bfs = []
bfs(v, visit, res_bfs)
print(' '.join(map(str, res_bfs)))