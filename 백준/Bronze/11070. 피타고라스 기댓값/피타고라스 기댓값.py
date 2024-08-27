t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    res = [[0,0] for x in range(n+1)]
    score = [0] * (n)
    for i in range(m) :
        a, b, p, q = map(int, input().split())
        res[a][0] += p
        res[a][1] -= q
        res[b][0] += q
        res[b][1] -= p
    for i in range(1, n+1) :
        if res[i][0] == res[i][1] == 0 :
            score[i-1] = 0
        else :
            score[i-1] = int(res[i][0] ** 2 / (res[i][0] ** 2 + res[i][1] ** 2) * 1000)
    print(max(score))
    print(min(score))