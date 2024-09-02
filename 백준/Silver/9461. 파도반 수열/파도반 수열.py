import sys

data = sys.stdin.read().splitlines()

t = int(data[0])

tab = [0] * 101

tab[1] = 1
tab[2] = 1
tab[3] = 1
tab[4] = 2
tab[5] = 2
tab[6] = 3

for x in range(6, 101) :
    tab[x] = tab[x-1] + tab[x-5]

for k in range(t) :
    print(tab[int(data[k+1])])