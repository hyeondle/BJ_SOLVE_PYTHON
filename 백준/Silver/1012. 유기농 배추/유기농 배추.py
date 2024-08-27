from collections import deque

def find_w(dp, m, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    count = 0

    def bfs(start_y, start_x):
        queue = deque()
        queue.append((start_y, start_x))
        dp[start_y][start_x] = 0  

        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and dp[ny][nx] == 1:
                    dp[ny][nx] = 0
                    queue.append((ny, nx))

    for y in range(n):
        for x in range(m):
            if dp[y][x] == 1:
                bfs(y, x)
                count += 1

    return count

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    dp = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        dp[y][x] = 1

    result = find_w(dp, m, n)
    print(result)

    