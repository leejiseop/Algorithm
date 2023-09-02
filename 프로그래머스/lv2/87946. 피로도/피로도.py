from itertools import permutations

def solution(k, dungeons):
    answer = [0]
    save = k
    for i in range(1, len(dungeons) + 1): # 1개씩 조합, 2개씩 조합, 3개씩 조합...
        p_list = list(permutations(dungeons, i))
        for p in p_list: # 3개씩 조합된것들
            for go in p: # 그 중 하나의 조합을 출발
                if go[0] <= k: # 필요 피로도보다 현재 피로도가 더 크면
                    k -= go[1] # 피로도 사용
                else:
                    break # 다음 조합 출발
                if k < 0:
                    break
            else: # 끝까지 도착
                if 1 <= k: # 남은 피로도가 1 이상이면
                    answer.append(i) # 성공경우의수 추가
            k = save # 피로도 복구

    return max(answer)