def caseof(a,b,c) :
    if a == b == c :
        return "Equilateral"
    s = max(a, b, c)
    k = min(a+b, b+c, c+a)
    if s >= k : return "Invalid"
    if a == b or b == c or c == a : return "Isosceles"
    else : return "Scalene"
    

while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    result = caseof(a,b,c)
    print(result)