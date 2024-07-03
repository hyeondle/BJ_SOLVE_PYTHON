import sys

data = sys.stdin.read().splitlines()
max_len = 0
lines = len(data)
c_d = []
temp = ""
for s in data :
    l = len(s)
    if l > max_len :
        max_len = l
for s in data :
    l = len(s)
    if l < max_len :
        for _ in range(max_len - l) :
            s += '-'
    c_d.append(s)
for _ in range(max_len) :
    for s in range(lines) :
        if c_d[s][_] == '-' : continue
        temp += c_d[s][_]
print(temp)