import sys
from collections import deque

# 1:10

f = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

data = []
n, k = map(int, f().split()) # 1~200, 1~1000
graph = []

for i in range(n):
  line = list(map(int, f().split()))
  graph.append(line)
  
  for j in range(n):
    if line[j] != 0:
      data.append((line[j], i, j, 0)) # virus, x, y, count

data.sort(key = lambda x: x[0])
q = deque(data)
time, find_x, find_y = map(int, f().split()) # 1~10000, 1 <= x y <= n

while q:
  virus, x, y, count = q.popleft()

  if time <= count:
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0:
      graph[nx][ny] = virus
      q.append((virus, nx, ny, count + 1))

print(graph[find_x - 1][find_y - 1])