import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])

radius = min(H, W) / 2

radius_cm = int(radius * 100)

print(radius_cm)