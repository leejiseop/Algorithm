from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    n = len(words)
    visited = [0 for _ in range(n)]
    q = deque()
    q.append([begin, 0])
    
    while q:
        now, cnt = q.popleft()
        
        if now == target:
            return cnt
        
        for i in range(n):
            diff = 0
            
            for c1, c2 in zip(now, words[i]):
                if c1 != c2:
                    diff += 1
                if 2 <= diff:
                    break
                    
            if diff == 1:
                if visited[i] == 0:
                    q.append([words[i], cnt + 1])
                else:
                    continue
    
    return 0