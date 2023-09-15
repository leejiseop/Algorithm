def solution(triangle):
    dp = []
    dp.append(triangle[0])
    
    for h in range(1, len(triangle)):
        layer = triangle[h]
        prev_dp_layer = dp[h - 1]
        new_dp_layer = [0 for i in layer]
        
        for i in range(len(prev_dp_layer)):
            left = prev_dp_layer[i] + layer[i]
            right = prev_dp_layer[i] + layer[i + 1]
            
            if new_dp_layer[i] < left:
                new_dp_layer[i] = left
            if new_dp_layer[i + 1] < right:
                new_dp_layer[i + 1] = right
                
        dp.append(new_dp_layer)
    
    return max(dp[-1])

# def solution(triangle):
#     dp = []
#     for t in range(1, len(triangle)):
#         for i in range(t+1):
#             if i == 0:
#                 triangle[t][0] += triangle[t-1][0]
#             elif i == t:
#                 triangle[t][-1] += triangle[t-1][-1]
#             else:
#                 triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
#     return max(triangle[-1])