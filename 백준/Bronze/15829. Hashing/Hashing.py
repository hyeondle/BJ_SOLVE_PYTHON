def compute_hash(s):
    r = 31
    M = 1234567891
    hash_value = 0

    for i, char in enumerate(s):
        a_i = ord(char) - ord('a') + 1
        hash_value += a_i * (r ** i)
        hash_value %= M
    
    return hash_value


n = int(input().strip())
s = input().strip()


result = compute_hash(s)


print(result)
