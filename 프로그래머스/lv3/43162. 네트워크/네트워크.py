def solution(n, computers):
    
    def dfs(com):
        visited[com] = True
        for connect in range(n):
            if computers[com][connect] == 1 and not visited[connect]:
                dfs(connect)
    
    answer = 0
    visited = [False for _ in range(n)]
    
    for com in range(n):
        if not visited[com]:
            dfs(com)
            answer += 1
    
    return answer












# def solution(n, computers):
    
#     def dfs(com):
#         visited[com] = True
#         for connect in range(n):
#             if computers[com][connect] == 1 and not visited[connect]:
#                 dfs(connect)
                
#     answer = 0
#     visited = [False for _ in range(n)]
    
#     for com in range(n):
#         if not visited[com]:
#             dfs(com)
#             answer += 1
    
#     return answer