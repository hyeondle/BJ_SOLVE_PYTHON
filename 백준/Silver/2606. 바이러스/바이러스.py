import sys
from collections import deque

data = sys.stdin.read().splitlines()

link = [set() for x in range(int(data[0]) + 1)] 
pc = [False for x in range(int(data[0]) + 1)]
pc[1] = True
count = 0

for _ in range(int(data[1])) :
    n, m = map(int, data[_ + 2].split())
    link[n].add(m)
    link[m].add(n)

queue = deque([1])

while(queue) :
    l = queue.popleft()

    for i in link[l] :
        if not pc[i] :
            queue.append(i)
            pc[i] = True
            count += 1
    
print(count)