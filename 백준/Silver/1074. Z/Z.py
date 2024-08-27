def find_z_value(n, r, c):
    value = 0
    size = 2 ** n

    while size > 1:
        size //= 2
        if r < size and c < size:
            value += 0
        elif r < size and c >= size:
            value += size * size
            c -= size
        elif r >= size and c < size:
            value += 2 * size * size
            r -= size
        else:
            value += 3 * size * size
            r -= size
            c -= size

    return value

n,r,c = map(int,input().split())

result = find_z_value(n, r, c)
print(result)