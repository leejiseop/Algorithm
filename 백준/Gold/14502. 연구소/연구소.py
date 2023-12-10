from collections import deque

n, m = list(map(int, input().split()))
graph = [ [0] * m for _ in range(n)]
temp = [ [0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
answer = 0

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(m):
    graph[i][j] = data[j]


def virus(temp, i, j):
  q = deque()
  q.append((i, j))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < m and temp[nx][ny] == 0:
        temp[nx][ny] = 3
        q.append((nx, ny))
        

def wall():
  global count
  global answer
  
  if count == 3:
    result = 0
    
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
    
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(temp, i, j)
          
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 0:
          result += 1
          
    answer = max(answer, result)
    
  else:
    for i in range(n):
      for j in range(m):
        if graph[i][j] == 0:
          graph[i][j] = 1
          count += 1
          wall()
          graph[i][j] = 0
          count -= 1

wall()
print(answer)