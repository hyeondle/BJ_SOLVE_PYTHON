import sys
import heapq
data = list(map(int,sys.stdin.read().splitlines()))
heap = []
for i in range(data[0]) :
    if data[i+1] == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap, (abs(data[i+1]), data[i+1]))