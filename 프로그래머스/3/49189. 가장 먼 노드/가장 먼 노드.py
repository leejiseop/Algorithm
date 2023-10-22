from collections import deque
def solution(n, edge):
    answer = 0
    
    # visited = [False] * n
    graph = [ [] for _ in range(n + 1)]
    dist = [-1 for _ in range(n + 1)]
    dist[1] = 0
    q = deque([1])
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    while q:
        p = q.popleft()
        
        for i in graph[p]:
            if dist[i] == -1:
                dist[i] = dist[p] + 1
                q.append(i)
    
    return dist.count(max(dist))