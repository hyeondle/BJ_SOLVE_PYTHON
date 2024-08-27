import sys
data = sys.stdin.read().splitlines()
for s in data :
    n, a, w = s.split()
    if n == '#' :
        break
    if int(a) > 17 or int(w) > 79 :
        print(n, "Senior")
    else :
        print(n, "Junior")