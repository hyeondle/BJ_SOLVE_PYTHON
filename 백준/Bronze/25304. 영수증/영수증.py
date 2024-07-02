s = int(input())
t = int(input())
for _ in range(t):
    p,a = map(int,input().split())
    s -= p*a
if s == 0 :
    print("Yes")
else :
    print("No")