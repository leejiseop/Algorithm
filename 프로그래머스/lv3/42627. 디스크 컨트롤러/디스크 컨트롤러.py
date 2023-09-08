import heapq

def solution(jobs):
    answer = 0
    now, i = 0, 0
    start = -1
    h = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(h, [j[1], j[0]])
        if 0 < len(h):
            current = heapq.heappop(h)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))