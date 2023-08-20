def solution(k, score):
    answer = []
    hof = []
    
    for s in score:
        hof.append(s)
        hof.sort(reverse = True)
        if k < len(hof):
            hof.pop()
        answer.append(hof[-1])
    return answer