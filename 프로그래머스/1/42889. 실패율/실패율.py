def solution(N, stages): # 6:00
    answer = []
    fail_ratio = [] # (stage, ratio)
    
    for i in range(1, N + 1):
        arrived = 0
        not_cleared = 0
        
        for stage in stages:
            if i <= stage:
                arrived += 1
            if i == stage:
                not_cleared += 1
        if arrived == 0:
            arrived = 1
        fail_ratio.append((i, not_cleared / arrived))
    fail_ratio.sort(key = lambda x: (-x[1], x[0]))
    
    return [i[0] for i in fail_ratio]
















# def solution(N, stages):
#     answer = []
#     score_list = []
    
#     for i in range(1, N + 1):
#         not_clear, arrived = 0, 0
#         for stage in stages:
#             if i <= stage:
#                 arrived += 1
#             if i == stage:
#                 not_clear += 1
#         if arrived == 0:
#             arrived = 1
#         score_list.append([i, (not_clear/arrived)])
        
#     score_list.sort(key = lambda x: (-x[1], x[0]))
#     answer = [i[0] for i in score_list]
    
#     return answer