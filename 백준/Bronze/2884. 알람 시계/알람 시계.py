h,m=input("").split()
h=int(h);m=int(m)
if m < 45:
    if h == 0 : h = 24
    print((h-1),(15+m))
else:
    print(h,m-45)