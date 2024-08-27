n = int(input())

for _ in range(n):
    t = int(input())
    clothes = {}
    
    for _ in range(t):
        item, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    

    combinations = 1
    for count in clothes.values():
        combinations *= (count + 1)

    combinations -= 1
    
    print(combinations)