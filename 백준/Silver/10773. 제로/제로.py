import sys
data = sys.stdin.read().splitlines()

n = int(data[0])
stack = []
for _ in range(n) :
    if int(data[_+1]) == 0 :
        stack.pop()
    else :
        stack.append(int(data[_+1]))
print(sum(stack))
