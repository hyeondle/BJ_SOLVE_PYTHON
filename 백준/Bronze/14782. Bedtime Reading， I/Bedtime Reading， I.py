import math
n = int(input())

k = int(math.sqrt(n))
sum = 0
for i in range(k) :
    if n % (i + 1) == 0 :
        sum += i+1 + n // (i+1)
print(sum)