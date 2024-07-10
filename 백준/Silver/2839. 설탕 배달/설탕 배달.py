t = int(input())
count = 0

while t >= 0:
    if t % 5 == 0:
        count += t // 5
        print(count)
        break
    t -= 3
    count += 1
else:
    print(-1)