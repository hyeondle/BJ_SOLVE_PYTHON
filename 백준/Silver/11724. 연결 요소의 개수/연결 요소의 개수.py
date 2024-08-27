import sys
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())

edges = []
for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    edges.append((u, v))

graph = [[] for _ in range(n + 1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def dfs(node):
    stack = [node]
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        count += 1

print(count)