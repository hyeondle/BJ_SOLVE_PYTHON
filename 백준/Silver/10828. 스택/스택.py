import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
stack = []
output = []

for i in range(1, n + 1):
    command = data[i]
    
    if command.startswith("push"):
        _, value = command.split()
        stack.append(value)
    elif command == "pop":
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)
    elif command == "size":
        output.append(len(stack))
    elif command == "empty":
        output.append(1 if not stack else 0)
    elif command == "top":
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)

print("\n".join(map(str, output)))