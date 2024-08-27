def count_colors(x, y, n):
    global white, blue
    color = paper[x][y]
    all_same = True
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                all_same = False
                break
        if not all_same:
            break
    
    if all_same:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        count_colors(x, y, half)
        count_colors(x, y + half, half)
        count_colors(x + half, y, half)
        count_colors(x + half, y + half, half)


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


white = 0
blue = 0


count_colors(0, 0, n)


print(white)
print(blue)
