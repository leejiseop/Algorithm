def solution(a, b):
    length = len(a)
    answer = 0
    for i in range(0, length):
        answer += a[i] * b[i]
        # zip 쓰자
    return answer