from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue
            

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

print(bfs(0, 0))

