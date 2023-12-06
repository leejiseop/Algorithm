from itertools import combinations

n, m = list(map(int, input().split()))
chickens, houses = [], []
distance = 987654321
result = 0
answer = 987654321

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 1:
      houses.append((i, j))
    elif line[j] == 2:
      chickens.append((i, j))

for combi in list(combinations(chickens, m)):
  for house in houses:
    for chicken in combi:
      distance = min(distance, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    result += distance
    distance = 987654321
  answer = min(answer, result)
  result = 0

print(answer)
