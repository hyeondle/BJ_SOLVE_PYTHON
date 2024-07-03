import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())

orders = []
for p in data[1:m+1] :
    i, j = map(int, p.split())
    orders.append((i, j))
baskets = list(range(1, n + 1))

def reverse_basket(baskets, i, j) :
    baskets[i-1:j] = reversed(baskets[i-1:j])

for order in orders :
    i, j = order
    reverse_basket(baskets, i, j)
    
print(" ".join(map(str, baskets)))