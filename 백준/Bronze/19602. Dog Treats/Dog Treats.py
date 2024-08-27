import sys

d = sys.stdin.read().splitlines()
sum = int(d[0]) + int(d[1]) * 2 + int(d[2]) * 3
if sum >= 10 :
    print('happy')
else :
    print('sad')