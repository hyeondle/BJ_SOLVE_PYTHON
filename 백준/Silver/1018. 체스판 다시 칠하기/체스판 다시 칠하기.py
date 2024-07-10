def find_least(data, start_x, start_y):
    pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
    pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4

    count1 = 0
    count2 = 0

    for i in range(8):
        for j in range(8):
            if data[start_x + i][start_y + j] != pattern1[i][j]:
                count1 += 1
            if data[start_x + i][start_y + j] != pattern2[i][j]:
                count2 += 1

    return min(count1, count2)

import sys
n, m = map(int, input().split())
data = sys.stdin.read().splitlines()

least = 64
for x in range(n - 7):
    for y in range(m - 7):
        t_min = find_least(data, x, y)
        if t_min < least:
            least = t_min

print(least)

        