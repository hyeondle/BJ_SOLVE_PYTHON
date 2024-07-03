b, c = map(int, input().split())
b = [0] * (b)
for i in range(c) :
    i, j, k = map(int, input().split())
    for index in range(i-1, j) :
        b[index] = k
print(' '.join(map(str,b)))