def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

prime_numbers = [i for i in range(M, N+1) if is_prime(i)]

if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)
