import sys
m = int(input())
S = 0
result = []

for _ in range(m):
    command = sys.stdin.readline().strip()
    if command == "all":
        S = (1 << 21) - 1
    elif command == "empty":
        S = 0
    else:
        cmd, x = command.split()
        x = int(x)
        
        if cmd == "add":
            S |= (1 << x)
        elif cmd == "remove":
            S &= ~(1 << x)
        elif cmd == "check":
            if S & (1 << x) :
                print(1)
            else :
                print(0)
        elif cmd == "toggle":
            S ^= (1 << x)