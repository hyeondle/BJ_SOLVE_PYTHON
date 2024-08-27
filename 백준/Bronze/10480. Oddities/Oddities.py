import sys
data=list(map(int,sys.stdin.read().splitlines()))
for _ in range(data[0]) :
    print(f'{data[_+1]} is {"odd" if data[_+1] %2 == 1 else "even"}')