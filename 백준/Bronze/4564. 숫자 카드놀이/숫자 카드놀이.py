import sys
d = sys.stdin.read().splitlines()

for s in d :
    if s == '0' :
        break
    print(s, end=' ')
    if len(s) == 1 :
        print()
        continue
    t = s
    while True :
        n = 1
        for c in t :
            n = n * int(c)
        print(n, end=' ')
        t = str(n)
        if len(t) == 1 :
            print()
            break
        
        