from collections import deque

def solution(n, wires): # 12:15 시작
    
    def bfs(here):
        cnt = 1
        q = deque([here])
        visited = [False for _ in range(n + 1)]
        
        while q:
            pop = q.popleft()
            
            for connect in graph[pop]:
                if not visited[connect]:
                    q.append(connect)
                    visited[pop] = True
                    cnt += 1
                
        return cnt
    
    answer = 1000
    graph = [ [] for _ in range(n + 1)]
    
    for r, l in wires:
        graph[r].append(l)
        graph[l].append(r)
        
    for r, l in wires:
        graph[r].remove(l)
        graph[l].remove(r)
        
        l_result = bfs(l)
        r_result = bfs(r)
        
        diff = abs(l_result - r_result)
        
        if diff < answer:
            answer = diff
        
        graph[r].append(l)
        graph[l].append(r)
        
    return answer