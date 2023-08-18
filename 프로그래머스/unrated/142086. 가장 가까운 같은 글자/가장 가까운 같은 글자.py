def solution(s):
    answer = []
    first = set()
    for i, c in enumerate(s):
        if c not in first:
            first.add(c)
            answer.append(-1)
        else:
            temp = s[:i]
            answer.append(temp[::-1].index(c) + 1)
    return answer