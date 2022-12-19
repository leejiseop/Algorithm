def solution(s):
    length = len(s)
    answer = (length == 4 or length == 6) and s.isnumeric()
    return answer