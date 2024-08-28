import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
trees = list(map(int, data[1].split()))

prev_min = 0
prev_max = max(trees)

while prev_min <= prev_max :
    cut = (prev_min + prev_max) // 2

    res = 0
    for i in trees :
        if i >= cut :
            res += i - cut
    if res >= m :
        prev_min = cut + 1        
    else :
        prev_max = cut - 1
print(prev_max)