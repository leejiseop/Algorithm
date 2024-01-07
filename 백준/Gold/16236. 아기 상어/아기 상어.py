# 10:57 11:10 

from collections import deque

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
size = 2
eat = 0
shark_x, shark_y = 0, 0

n = int(input())
graph = []

for i in range(n):
  line = list(map(int, input().split()))
  graph.append(line)
  for j in range(n):
    if line[j] == 9:
      shark_x, shark_y = i, j
      graph[i][j] = 0


'''
1. 상어 현 위치에서 bfs -> 새로운 그래프에 물고기까지의 거리 저장 ㅇㅇ
  나보다 큰 물고기는 지나갈 수 없다 -> 장애물 처리
2. 거리 그래프 i j 순회 -> 최소값 만날때마다 최소값, i, j저장
  이후 최소값과 같은 거리는 무시 -> 어차피 가장 좌상단 위치만 필요
3. 최소값을 결과에 더해주고 graph[i][j] = 0 처리 -> 물고기 먹음
4. 순회 돌았는데 없으면 끝

자신의 크기보다 작은 물고기만 먹을 수 있다
크기가 같은 물고기는 먹을 수 없지만, 지나갈 수 있다.
'''

def bfs(x, y):
  dist = [ [INF] * n for _ in range(n)]
  q = deque()
  
  q.append((x, y))
  dist[x][y] = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not (0 <= nx < n) or not (0 <= ny < n):
        continue
      if dist[nx][ny] == INF and graph[nx][ny] <= size:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))
        
  return dist

def find(dist):
  fish_x, fish_y = -1, -1
  fish_dist = INF
  
  for i in range(n):
    for j in range(n):
      if dist[i][j] < fish_dist and (1 <= graph[i][j] < size):
        fish_x, fish_y = i, j
        fish_dist = dist[i][j]

  return [fish_x, fish_y, fish_dist]
  
while True:
  
  dist = bfs(shark_x, shark_y)
  
  target_x, target_y, target_dist = find(dist)
  
  if target_dist == INF:
    break
    
  shark_x, shark_y = target_x, target_y
  graph[target_x][target_y] = 0
  answer += target_dist
  eat += 1
  
  if eat == size:
    eat = 0
    size += 1

print(answer)