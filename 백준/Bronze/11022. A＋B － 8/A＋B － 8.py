import sys
input = sys.stdin.read

data = input().split('\n')
for i in range(int(data[0])):
    a, b = map(int, data[i+1].split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
