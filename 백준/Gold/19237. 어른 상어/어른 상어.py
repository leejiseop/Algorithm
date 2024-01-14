# 1:00 1:20(샤워)
# 12:05 12:40
# 12:50 

# graph 냄새 지도(상어번호, 남은시간) 2차원배열
# sharks 현재 상어i 정보 배열 (x, y, d)
# priority 우선순위 3차원 배열[상어번호i][현재방향(상하좌우)] = [우선순위] 리스트
# shark_count 남은 상어 마리수
# time 소요시간

# 실수 정리
# 가려는곳이 살아있는 상어인지 죽어있는 상어인지 체크 못함.

def new_smell(graph):
  # 현 위치에 새로운 냄새 뿌리기
  for shark_num in range(1, m + 1):
    x, y, d = sharks[shark_num]
    if d == -100:
      continue
    graph[x][y][0] = shark_num
    graph[x][y][1] = k


def smell_minus(graph):
  # 전체 냄새 줄어들면서 냄새가 0이 되면 상어 정보도 0
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if 1 <= graph[i][j][1]:
        graph[i][j][1] -= 1
        if graph[i][j][1] == 0:
          graph[i][j][0] = 0
        


def move_shark(shark_num, next_position):
  # 상어 이동시 상어리스트 돌면서
  # 내가 가려는 곳에 나보다 큰 상어 있으면 쫒겨나고(d = -1)
  # shark_count -= 1
  # 상어 정보 갱신

  global shark_count

  nx, ny, nd = next_position # 가려는 곳
  for upper_shark_num in range(1, shark_num):
    ux, uy, ud = sharks[upper_shark_num]
    if ud != -100 and ux == nx and uy == ny: # 가려는 곳에 나보다 '살아있는'!! 상위 상어가 있으면
      sharks[shark_num][2] = -100 # 이동하려던 상어는 쫒겨남
      shark_count -= 1
      return
  sharks[shark_num][0] = nx
  sharks[shark_num][1] = ny
  sharks[shark_num][2] = nd
    


def find_my(shark_num):
  # 주변 자기냄새 찾기 (현재 방향 기준 우선순위 순으로 탐색하고, 찾으면 바로 반환)
  position = []
  x, y, d = sharks[shark_num]
  for p_d in priority[shark_num][d - 1]:
    nx = x + dx[p_d - 1]
    ny = y + dy[p_d - 1]
    if not (1 <= nx <= n) or not (1 <= ny <= n):
      continue
    if graph[nx][ny][0] == shark_num:
      position = [nx, ny, p_d]
      break
  
  return position
  

def find_blank(shark_num):
  # 주변 빈칸 찾기 (현재 방향 기준 우선순위 순으로 탐색하고, 찾으면 바로 반환)
  position = []
  x, y, d = sharks[shark_num]
  for p_d in priority[shark_num][d - 1]:
    nx = x + dx[p_d - 1]
    ny = y + dy[p_d - 1]
    if not (1 <= nx <= n) or not (1 <= ny <= n):
      continue
    if graph[nx][ny][0] == 0:
      position = [nx, ny, p_d]
      break
  
  return position


dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] # 0 1 2 3

n, m, k = map(int, input().split())

graph = [ [ [0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
sharks = [ [] for _ in range(m + 1)]
priority = [ [] for _ in range(m + 1)]
shark_count = m
time = 0

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] != 0:
      sharks[line[j]] = [i + 1, j + 1]

first_direction = list(map(int, input().split()))
for i in range(1, m + 1):
  shark_i_direction = first_direction[i - 1]
  sharks[i].append(shark_i_direction)

for i in range(1, m + 1):
  for _ in range(4):
    line = list(map(int, input().split()))
    priority[i].append(line)

# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
new_smell(graph)

# 그 후
while True:
  # print('turn ' + str(time))
  # for i in range(1, n + 1):
  #   # line = [c[0] if c[1] == k else 0 for c in graph[i][1:]]
  #   # print(line)
  #   print(graph[i][1:])
  # print(sharks)
  # print()
  if 1000 < time:
    print(-1)
    break
  if shark_count == 1:
    print(time)
    break
  for shark_num in range(1, m + 1):
    x, y, d = sharks[shark_num]
    if d == -100:
      continue
    next_position = find_blank(shark_num)
    if not next_position:
      next_position = find_my(shark_num)
    if next_position:
      move_shark(shark_num, next_position)
  smell_minus(graph)
  new_smell(graph)
  time += 1

'''
test case
https://www.acmicpc.net/board/view/52566
'''




