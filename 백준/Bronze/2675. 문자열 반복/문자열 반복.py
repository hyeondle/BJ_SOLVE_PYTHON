case = int(input())

for _ in range(case) :
    r, s = input().split()
    r = int(r)
    x = ''.join(c * r for c in s)
    print(x)

