import sys
import heapq
data = list(map(int,sys.stdin.read().splitlines()))
heap = []
for i in range(data[0]) :
    if data[i+1] == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap, data[i+1])