import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
queue = []
output = []

for i in range(1, n + 1):
    command = data[i]
    
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        if queue:
            output.append(queue.pop(0))
        else:
            output.append(-1)
    elif command == "size":
        output.append(len(queue))
    elif command == "empty":
        output.append(1 if not queue else 0)
    elif command == "front":
        if queue:
            output.append(queue[0])
        else:
            output.append(-1)
    elif command == "back":
        if queue:
            output.append(queue[-1])
        else:
            output.append(-1)

print("\n".join(map(str, output)))
