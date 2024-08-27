import sys

data = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(data) :
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)) :
    if arr[i] != 0 :
        for _ in range(arr[i]) :
            print(i)