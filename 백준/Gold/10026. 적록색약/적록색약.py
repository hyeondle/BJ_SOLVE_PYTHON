from collections import deque

def bfs(x, y, tab, visited, n):
    queue = deque([(x, y)])
    color = tab[x][y]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if tab[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

n = int(input())
tab = [list(input().replace('R', '1').replace('G', '2').replace('B', '3')) for _ in range(n)]
tab = [[int(color) for color in row] for row in tab]

tab_colorblind = [[color if color != 1 else 2 for color in row] for row in tab]

visited_normal = [[False] * n for _ in range(n)]
visited_colorblind = [[False] * n for _ in range(n)]

normal_count = 0
colorblind_count = 0

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            bfs(i, j, tab, visited_normal, n)
            normal_count += 1
        if not visited_colorblind[i][j]:
            bfs(i, j, tab_colorblind, visited_colorblind, n)
            colorblind_count += 1

print(normal_count, colorblind_count)