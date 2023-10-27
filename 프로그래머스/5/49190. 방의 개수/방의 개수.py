def solution(arrows):
    graph = {str([0, 0]): []}
    move = [(-2, 0), (-2, 2), (0, 2), (2, 2), (2, 0), (2, -2), (0, -2), (-2, -2)] # 01234567
    now_x, now_y = 0, 0 # 그냥 변수 2개로 바꾸자
    to1_x, to1_y = 0, 0
    to2_x, to2_y = 0, 0
    answer = 0
    
    for arrow in arrows:
        to1_x, to1_y = now_x + move[arrow][0]//2, now_y + move[arrow][1]//2
        to2_x, to2_y = now_x + move[arrow][0], now_y + move[arrow][1]
        
        if str([to1_x, to1_y]) in graph:
            if not [now_x, now_y] in graph[str([to1_x, to1_y])]:
                graph[str([to1_x, to1_y])].append([now_x, now_y])
                graph[str([now_x, now_y])].append([to1_x, to1_y])
                answer += 1
        else:
            graph[str([to1_x, to1_y])] = [[now_x, now_y]]
            graph[str([now_x, now_y])].append([to1_x, to1_y])
            
        if str([to2_x, to2_y]) in graph:
            if not [to1_x, to1_y] in graph[str([to2_x, to2_y])]:
                graph[str([to2_x, to2_y])].append([to1_x, to1_y])
                graph[str([to1_x, to1_y])].append([to2_x, to2_y])
                answer += 1
        else:
            graph[str([to2_x, to2_y])] = [[to1_x, to1_y]]
            graph[str([to1_x, to1_y])].append([to2_x, to2_y])

        now_x, now_y = to2_x, to2_y
        
    return answer