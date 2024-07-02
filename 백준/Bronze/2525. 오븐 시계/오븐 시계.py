h,m=input("").split()
r=int(input(""))
h=int(h);m=int(m)
r += h*60 + m
p_h = r//60
p_m = r%60
if p_h > 23 : p_h %= 24
print(p_h, p_m)