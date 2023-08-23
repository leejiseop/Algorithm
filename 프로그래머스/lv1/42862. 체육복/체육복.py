def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for student in lost:
        if student in reserve:
            reserve.pop(reserve.index(student))
            lost.pop(lost.index(student))
    
    for student in lost:
        if student in reserve:
            reserve[reserve.index(student)] = 'o'
            lost[lost.index(student)] = 'o'
        elif student - 1 in reserve:
            reserve[reserve.index(student - 1)] = 'o'
            lost[lost.index(student)] = 'o'
        elif student + 1 in reserve:
            reserve[reserve.index(student + 1)] = 'o'
            lost[lost.index(student)] = 'o'
    
    return n - len(lost) + lost.count('o')

