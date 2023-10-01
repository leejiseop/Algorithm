from collections import deque

def solution(maps):
    dx = [-1,1,0 ,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return maps[x][y]
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        q.append((nx, ny))
                        maps[nx][ny] = maps[x][y] + 1
                        print(x, y, nx, ny)
    
    return -1