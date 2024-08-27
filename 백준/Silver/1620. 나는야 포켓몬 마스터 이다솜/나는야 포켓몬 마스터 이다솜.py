import sys

data = sys.stdin.read().splitlines()

m,n = map(int, data[0].split())

l = data[1:1+m]
q = data[1+m:]

dics = {}
dicn = {}

for i in range(m) :
    dics[l[i]] = i+1
    dicn[i+1] = l[i]

res = []

for a in q :
    if a.isdigit() :
        res.append(dicn.get(int(a)))
    else :
        res.append(str(dics.get(a)))
sys.stdout.write('\n'.join(res)+'\n')