import sys

data = sys.stdin.read().splitlines()

submitted = set(map(int,data))
students = set(range(1,31))
n_submitted = students - submitted

print(min(n_submitted))
print(max(n_submitted))