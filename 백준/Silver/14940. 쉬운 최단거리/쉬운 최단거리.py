from collections import deque

n, m = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

start_x = start_y = 0
for i in range(n):
    for j in range(m):
        if t[i][j] == 2:
            start_y, start_x = i, j

queue = deque([(start_y, start_x)])
dp[start_y][start_x] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m and dp[ny][nx] == -1:
            if t[ny][nx] == 1:
                dp[ny][nx] = dp[y][x] + 1
                queue.append((ny, nx))
            elif t[ny][nx] == 0:
                dp[ny][nx] = 0


for y in range(n) :
    for x in range(m) :
        if t[y][x] == 0 and dp[y][x] == -1 :
            dp[y][x] = 0
for row in dp:
    print(' '.join(map(str, row)))

