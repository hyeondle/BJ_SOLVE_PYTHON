import sys

n = int(sys.stdin.read())

for i in range(n):
    print(f"{' '*(n-i-1)}{'*'*(i+1)}")