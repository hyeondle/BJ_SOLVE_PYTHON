import sys
data = sys.stdin.read().splitlines()

a,b = map(int,data[0].split())
m = a*b
l = list(map(int,data[1].split()))
for i in range(5) :
    print(l[i]-m)