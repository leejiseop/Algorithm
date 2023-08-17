def solution (number) :
    from itertools import combinations
    cnt = 0
#   combination 함수 알아두면 편할 것 같다
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt