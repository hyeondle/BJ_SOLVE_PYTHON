def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if grid[x][y] == 1:
        grid[x][y] = 0
        global count
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

num_of_complexes = 0
sizes_of_complexes = []


for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            sizes_of_complexes.append(count)
            num_of_complexes += 1

print(num_of_complexes)
for size in sorted(sizes_of_complexes):
    print(size)