import sys

data = sys.stdin.read().splitlines()

n,m = map(int, data[0].split())

A = []
B = []

for i in range(1, n+1) :
    row = list(map(int, data[i].split()))
    A.append(row)
for i in range(n+1, 2*n+1) :
    row = list(map(int, data[i].split()))
    B.append(row)

result = []
for i in range(n):
    row_result = []
    for j in range(m):
        sum_value = A[i][j] + B[i][j]
        row_result.append(sum_value)
    result.append(row_result)

for row in result:
    print(' '.join(map(str, row)))
