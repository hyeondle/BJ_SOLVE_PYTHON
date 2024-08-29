import sys
from collections import deque

data = sys.stdin.read().splitlines()

m, n = map(int, data[0].split())

tab = []
for _ in range(n):
    tab.append(list(map(int, data[_ + 1].split())))

def bfs():
    queue = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if tab[i][j] == 1:
                queue.append((i, j, 0))
    
    max_days = 0
    

    while queue:
        x, y, day = queue.popleft()
        max_days = max(max_days, day)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and tab[nx][ny] == 0:
                tab[nx][ny] = 1
                queue.append((nx, ny, day + 1))

    for row in tab:
        if 0 in row:
            return -1
    
    return max_days

result = bfs()
print(result)