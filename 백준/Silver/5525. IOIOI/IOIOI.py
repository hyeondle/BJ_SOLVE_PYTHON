n = int(input())
m = int(input())
s = input()

pattern_length = 2 * n + 1
count = 0
i = 0
result = 0

while i < (m - 1):
    if s[i:i+3] == 'IOI':
        count += 1
        if count == n:
            count -= 1
            result += 1
        i += 2
    else:
        count = 0
        i += 1

print(result)
