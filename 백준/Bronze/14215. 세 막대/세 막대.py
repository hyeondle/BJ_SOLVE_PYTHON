a,b,c = map(int, input().split())

r = max(a,b,c)
k = min(a+b,b+c,c+a)

if k > r :
    print(r+k)
else :
    print(2*k-1)