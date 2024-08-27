from collections import deque

def bfs(start, target):
    max_limit = 100000 #점의 범위
    visited = [False] * (max_limit + 1) #모든 범위를 먼저 미방문으로 채움
    queue = deque([(start, 0)])
    
    while queue:
        position, time = queue.popleft()
        
        if position == target:
            return time
        
        for next_pos in (position - 1, position + 1, position * 2):
            if 0 <= next_pos <= max_limit and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

n, k = map(int, input().split())
print(bfs(n, k))