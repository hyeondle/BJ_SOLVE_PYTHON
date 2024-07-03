import sys

data = sys.stdin.read().splitlines()

n = int(data[0])
scores = list(map(int, data[1].split()))

max_score = max(scores)
new_scores = []

for score in scores :
    new_scores.append(score / max_score * 100)

print(sum(new_scores)/n)