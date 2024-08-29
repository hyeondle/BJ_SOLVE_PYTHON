import sys
from collections import deque

data = sys.stdin.read().splitlines()

m, n, h = map(int, data[0].split())

tab = []
for i in range(h):
    tab.append([list(map(int, data[i * n + j + 1].split())) for j in range(n)])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tab[z][x][y] == 1:
                    queue.append((z, x, y, 0))
    
    max_days = 0 
    
    while queue:
        z, x, y, day = queue.popleft()
        max_days = max(max_days, day)
        
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tab[nz][nx][ny] == 0:
                tab[nz][nx][ny] = 1
                queue.append((nz, nx, ny, day + 1))

    for layer in tab:
        for row in layer:
            if 0 in row:
                return -1
    
    return max_days

result = bfs()
print(result)