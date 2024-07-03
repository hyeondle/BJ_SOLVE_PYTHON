import sys

data = sys.stdin.read().splitlines()

nums = list(map(int, data))
mods = []
for num in nums :
    mods.append(num % 42)

mods = set(mods)
print(len(mods))