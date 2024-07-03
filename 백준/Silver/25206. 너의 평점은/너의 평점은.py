import sys

state = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

sum_s = 0
sum_g = 0

data = sys.stdin.read().splitlines()

for s in data :
    t = s.split()
    if t[2] == 'P' : continue
    sum_s += float(t[1])
    sum_g += float(t[1]) * state[t[2]]

print(sum_g / sum_s)