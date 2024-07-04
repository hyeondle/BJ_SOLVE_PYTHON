import sys

def can_divide(t, test, b) :
    count = 0
    for num in t:
        count += num // test
    return count >= b

input = sys.stdin.read().splitlines()
a, b = map(int, input[0].split())
t = list(map(int, input[1:a+1]))

left = 1
right = max(t)
    
while left <= right:
    mid = (left + right) // 2
    if can_divide(t, mid, b):
        left = mid + 1
    else:
        right = mid - 1
            
print(right)