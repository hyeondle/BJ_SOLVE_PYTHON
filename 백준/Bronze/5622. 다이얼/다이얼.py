counts = []
for i in range(2, 10) :
    times = 3
    k = i + 1
    if i == 7 or i == 9 :
        times += 1
    for _ in range(times) :
        counts.append(k)
o = input()
sum = 0
for char in o :
    t = ord(char) - ord('A')
    sum += counts[t]
print(sum)