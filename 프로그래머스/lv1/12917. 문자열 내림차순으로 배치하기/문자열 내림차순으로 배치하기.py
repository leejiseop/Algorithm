def solution(s):
    list_s = list(s)
    list_s.sort()
    list_s.reverse()
    return ''.join(list_s)