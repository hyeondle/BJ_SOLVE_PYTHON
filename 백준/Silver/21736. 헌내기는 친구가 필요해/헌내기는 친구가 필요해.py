from collections import deque

n, m = map(int, input().split())

tab = [list(map(int, input().replace('O', '0').replace('X','1').replace('I','3').replace('P','4'))) for _ in range(n)]

x = y = 0
for i in range(n) :
    for j in range(m) :
        if tab[i][j] == 3 :
            x = i
            y = j
            break

def bfs(x, y) :
    queue = deque()

    queue.append((x,y))
    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    
    while queue :
        x, y = queue.popleft()
        for d in range(4) :
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if tab[nx][ny] == 1 :
                    continue
                visited[nx][ny] = True
                if tab[nx][ny] == 0 :
                    queue.append((nx,ny))
                elif tab[nx][ny] == 4 :
                    queue.append((nx,ny))
                    count += 1

    return count
count = bfs(x,y)
print(count if count > 0 else "TT")