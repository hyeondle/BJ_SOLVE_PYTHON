sets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k, c = map(int, input().split())
ans = ""
while k > 0 :
    t = k % c
    k = k // c
    ans = sets[t] + ans

print(ans)