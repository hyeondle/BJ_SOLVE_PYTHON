n = int(input())
x_max = -10000
y_max = -10000
x_min = 10000
y_min = 10000
for _ in range(n) :
    a, b = map(int, input().split())
    if a > x_max :
        x_max = a
    if a < x_min :
        x_min = a
    if b > y_max :
        y_max = b
    if b < y_min :
        y_min = b
print((x_max-x_min)*(y_max-y_min))
    