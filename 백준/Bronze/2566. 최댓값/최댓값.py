import sys

data = sys.stdin.read().splitlines()

table = []
r_max = 0
column = 0

for i in range(9) :
    row = list(map(int, data[i].split()))
    table.append(row)
    t_max = max(row)
    if t_max > r_max : r_max = t_max; column = i
print(r_max)
print(column+1, table[column].index(r_max)+1)
