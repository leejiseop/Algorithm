# 5:22

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

found_student = True
n = int(input()) # 3 <= n <= 6
graph = []
teacher_list = []
for i in range(n):
  line = list(input().split())
  graph.append(line)
  for j in range(n):
    if line[j] == 'T':
      teacher_list.append((i, j))


def observe(x, y):
  # up
  nx, ny = x, y
  while True:
    nx -= 1
    if 0 <= nx < n:
      if graph[nx][ny] == 'O':
        break
      elif graph[nx][ny] == 'S':
        return True
    else:
      break
  # down
  nx, ny = x, y
  while True:
    nx += 1
    if 0 <= nx < n:
      if graph[nx][ny] == 'O':
        break
      elif graph[nx][ny] == 'S':
        return True
    else:
      break
  # left
  nx, ny = x, y
  while True:
    ny -= 1
    if 0 <= ny < n:
      if graph[nx][ny] == 'O':
        break
      elif graph[nx][ny] == 'S':
        return True
    else:
      break
  # right
  nx, ny = x, y
  while True:
    ny += 1
    if 0 <= ny < n:
      if graph[nx][ny] == 'O':
        break
      elif graph[nx][ny] == 'S':
        return True
    else:
      break
  
  return False


def dfs(count):
  # print('dfs')
  global found_student
  
  if count == 3:
    for x, y in teacher_list:
      if observe(x, y):
        break
    else:
      found_student = False
  else:
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'X':
          graph[i][j] = 'O'
          dfs(count + 1)
          graph[i][j] = 'X'

dfs(0)
if not found_student:
  print('YES')
else:
  print('NO')