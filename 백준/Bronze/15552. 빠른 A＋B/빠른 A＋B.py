import sys

read = sys.stdin.read

data = read().splitlines()
results = []

for i in range(int(data[0])):
    a,b=map(int,data[i+1].split())
    results.append(a+b)

sys.stdout.write('\n'.join(map(str, results)) + '\n')