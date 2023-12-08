from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    
    # length = 5
    # weak = [1, 3, 4, 9, 10, / 13, 15, 16, 21, 22]
    # dist = [3, 5, 7]
    # start : 0 1 2 3 4
    for start in range(length): # 0부터 length - 1 까지의 위치를 각각 시작점으로 설정
        for friends in list(permutations(dist, len(dist))): # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
            count = 1 # 투입할 친구의 수
            position = weak[start] + friends[count - 1] # 해당 친구가 점검할 수 있는 마지막 위치 (start ~ position)
            for index in range(start, start + length): # 시작점부터 한바퀴 돌면서 모든 취약 지점을 확인
                if position < weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1 # 새로운 친구를 투입
                    if len(dist) < count: # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1] # 그 지점부터 다시 친구 범위만큼 position 증가
            answer = min(answer, count) # 최솟값 계산
            
    if len(dist) < answer:
        return -1
    
    return answer