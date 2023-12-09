from collections import deque
import sys
f = sys.stdin.readline

# 12:10

n, m, dist, x = list(map(int, f().split()))

visited = [False] * (n + 1)
graph = [ [] for _ in range(n + 1)]

for _ in range(m):
  a, b = list(map(int, f().split()))
  graph[a].append(b)
  

def bfs(start):
  result = []
  q = deque()
  q.append((start, 0))
  visited[start] = True

  while q:
    now, cnt = q.popleft()
    
    for connect in graph[now]:
      if not visited[connect]:
        visited[connect] = True
        if cnt + 1 == dist:
          result.append(connect)
          continue
        q.append((connect, cnt + 1))

  if len(result) == 0:
    print(-1)
  else:
    result.sort()
    for i in result:
        print(i, end='\n')
      

bfs(x)
