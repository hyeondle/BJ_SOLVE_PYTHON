mat = [[0] * 100 for _ in range(100)]

count = int(input())
for i in range(count) :
    x, y = map(int, input().split())
    for k in range(10) :
        if (y + k) > 100 : continue
        for j in range(10) :
            if (x + j) > 100 : continue
            mat[x+j][y+k] = 1
            
count = 0;
for i in range(100) :
    for j in range(100) :
        if mat[i][j] == 1 :
            count += 1
print(count)