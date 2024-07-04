c = int(input())
q = 25
d = 10
n = 5
p = 1
for _ in range(c) :
    t = int(input())
    s_a = t // q; t = t % q
    s_b = t // d; t = t % d
    s_c = t // n; t = t % n
    s_d = t // p
    print(s_a,s_b,s_c,s_d)