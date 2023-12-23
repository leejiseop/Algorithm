n = int(input()) # 3:00
left = 0
up = 0
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(i + 1):
    if 0 <= j - 1:
      left = graph[i - 1][j - 1]
    if j < i:
      up = graph[i - 1][j]
    graph[i][j] += max(left, up)

print(max(graph[-1]))