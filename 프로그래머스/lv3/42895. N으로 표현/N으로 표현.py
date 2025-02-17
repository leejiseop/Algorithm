def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1, 9):
        all_case = set()
        all_case.add(int(str(N) * i))
        
        for pair in range(0, i - 1):
            for left in dp[pair]:
                for right in dp[-1 - pair]:
                    all_case.add(left + right)
                    all_case.add(left - right)
                    all_case.add(left * right)
                    if right != 0:
                        all_case.add(left / right)
        if number in all_case:
            answer = i
            break
        else:
            dp.append(all_case)
    
    return answer












# def solution(N, number):
#     answer = -1
#     dp = []
    
#     for cnt in range(1, 9): # 1개부터 8개까지 확인
#         all_case = set()
#         all_case.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        
#         for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
#             for op1 in dp[i]:
#                 for op2 in dp[-i - 1]:
#                     all_case.add(op1 + op2)
#                     all_case.add(op1 * op2)
#                     all_case.add(op1 - op2)
#                     if op2 != 0:
#                         all_case.add(op1 / op2)
                        
#         # 만든 집합에 number가 처음 나오는지 확인
#         if number in all_case:
#             answer = cnt
#             break
#         dp.append(all_case)
        
#     return answer
