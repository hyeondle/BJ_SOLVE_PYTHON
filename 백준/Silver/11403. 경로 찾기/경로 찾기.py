import sys

data = sys.stdin.read().splitlines()

n = int(data[0])
INF = 10000000
tab = [list(map(int,data[x+1].replace('0', '10000000').split())) for x in range(n)]

for k in range(n) :
    for x in range(n) :
        for y in range(n) :
            if tab[x][y] > tab[x][k] + tab[k][y] :
                tab[x][y] = tab[x][k] + tab[k][y]

for x in range(n) :
    for y in range(n) :
        if tab[x][y] == 10000000 :
            if y == n-1 :
                print(0, end='')
            else :
                print(0, end=' ')
        else :
            if y == n-1 :
                print(1, end='')
            else :
                print(1, end=' ')
    if x == n-1 :
        break
    print()