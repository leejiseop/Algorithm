def solution(n, results): # 11:14 이거 풀고 바로 샤워
    answer = 0
    graph = [ [0] * (n + 1) for _ in range(n + 1)]
    
    c_sum = [0] * (n + 1)
    r_sum = [0] * (n + 1)
    
    for win, lose in results:
        graph[win][lose] = 1
    
    for k in range(1, n + 1):
        for win in range(1, n + 1):
            for lose in range(1, n + 1):
                if graph[win][lose] == 0 and graph[win][k] == 1 and graph[k][lose] == 1:
                    graph[win][lose] = 1
    
    for win in range(1, n + 1):
        for lose in range(1, n + 1):
            c_sum[lose] += graph[win][lose]
            r_sum[win] += graph[win][lose]
            
    for i in range(1, n + 1):
        if c_sum[i] + r_sum[i] == n - 1:
            answer += 1
    
    return answer






# def solution(n, results): # 플로이드 워셜
#     answer = 0
#     board = [[0]*n for _ in range(n)]
    
#     for a,b in results:
#         board[a-1][b-1] = 1
#         board[b-1][a-1] = -1
        
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i == j or board[i][j] in [1,-1]:
#                     continue
#                 if board[i][k] == board[k][j] == 1:
#                     board[i][j] = 1
#                     board[j][i] = board[k][i] = board[j][k] = -1
#     for row in board:
#         if row.count(0) == 1:
#             answer += 1
#     return answer