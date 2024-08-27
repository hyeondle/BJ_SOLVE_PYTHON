import sys
t = "abcdefghijklmnopqrstuvwxyz"
data = sys.stdin.read().lower().splitlines()

for _ in range(int(data[0])) :
    miss = []
    for x in t :
        if data[_+1].find(x) >= 0 :
            continue
        else :
            miss.append(x)
    if miss == [] :
        print('pangram')
    else :
        print(f'missing {"".join(map(str,miss))}')