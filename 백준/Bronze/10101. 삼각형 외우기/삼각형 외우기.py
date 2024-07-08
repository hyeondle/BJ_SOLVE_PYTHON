import sys
data = sys.stdin.read().splitlines()

a, b, r = int(data[0]), int(data[1]), int(data[2])
s = a + b + r

if s != 180:
    print("Error")
elif a == 60 and b == 60 and r == 60:
    print("Equilateral")
elif a == b or b == r or r == a:
    print("Isosceles")
else:
    print("Scalene")
