def prime_factors(n):
    factor = 2
    factors = []
    while factor * factor <= n:
        while (n % factor) == 0:
            factors.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.append(n)
    return factors

N = int(input())

if N > 1:
    factors = prime_factors(N)
    for factor in factors:
        print(factor)
