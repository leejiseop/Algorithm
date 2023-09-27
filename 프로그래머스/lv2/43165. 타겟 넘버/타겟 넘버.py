def solution(numbers, target):
    answer = 0
    end = len(numbers)
    
    def dfs(idx, result):
        if idx == end:
            if result == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])
        
    dfs(0, 0)
    
    return answer


# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
#     dfs(0,0)
#     return answer