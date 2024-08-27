import sys
data = list(map(int, sys.stdin.read().splitlines()))

n = data[0]
data = data[1:]
sa = mid = mfr = ran = 0

sa = int(round((sum(data) / n), 0))
data = sorted(data)
mid = data[n//2]
dset = set(data)

from collections import Counter

counter = Counter(data)
frelis = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

if len(frelis) > 1 and frelis[0][1] == frelis[1][1]:
    mfr = frelis[1][0]
else:
    mfr = frelis[0][0]
        
ran = max(data) - min(data)

result = str(sa)+'\n'+str(mid)+'\n'+str(mfr)+'\n'+str(ran)+'\n'
print(result)