def solution(k, m, score):
    answer = 0
    score.sort()
    score.reverse()
    
    for i, apple in enumerate(score, start = m):
        if (i + 1) % m == 0:
            answer += apple * m
            
    return answer