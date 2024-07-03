import sys

data = list(map(int,sys.stdin.read().splitlines()))

print(max(data))
print(data.index(max(data))+1)