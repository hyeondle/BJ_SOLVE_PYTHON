while True:
    n = int(input())
    if n == -1 :
        break
    k = []
    for j in range(n-1):
        if n % (j+1) == 0 :
            k.append((j+1))
    if sum(k) == n :
        print(f"{n} = {' + '.join(map(str, k))}")
    else :
        print(f'{n} is NOT perfect.')