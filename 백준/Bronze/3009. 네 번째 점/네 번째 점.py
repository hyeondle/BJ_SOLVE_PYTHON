import sys

data = sys.stdin.read().splitlines()

a, b = map(int, data[0].split())
c, d = map(int, data[1].split())
e, f = map(int, data[2].split())

x = [a, c, e]
y = [b, d, f]

x_min = min(x)
y_min = min(y)
x_max = max(x)
y_max = max(y)

strs = ""

if x.count(x_min) == 1 :
    strs += str(x_min)
else :
    strs += str(x_max)
strs += " "
if y.count(y_min) == 1 :
    strs += str(y_min)
else :
    strs += str(y_max)
    
print(strs)
