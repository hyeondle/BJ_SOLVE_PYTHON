import sys

data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
tab = {}
for i in range(n) :
    key, value = map(str, data[i+1].split())
    tab[key] = value

for i in range(m) :
    print(tab.get(data[1+n+i]))