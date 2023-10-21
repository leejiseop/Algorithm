# https://mjmjmj98.tistory.com/109

def solution(money):
    money_length = len(money)
    dp1 = [0 for _ in range(money_length)]
    dp2 = [0 for _ in range(money_length)]
    # n = n-2최대값 + 자신
    dp1[0], dp1[1] = money[0], money[0]
    dp2[0], dp2[1] = 0, money[1]
    
    for i in range(2, money_length - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    for i in range(2, money_length):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        
    return max(dp1[-2], dp2[-1])









# def solution(money):
#     dp1 = [0] * len(money)
#     dp2 = [0] * len(money)
#     # 1번 집을 터는 경우
#     dp1[0] = money[0]
#     for i in range(1, len(money) - 1):  # 마지막 집은 털지 못함
#         dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
#     # 1번 집을 안터는 경우
#     dp1[0] = 0
#     for i in range(1, len(money)):
#         dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

#     return max(dp1[-2], dp2[-1])


# def solution(money):
#     answer = 0 # 이거 안됨 ---> 블로그 글에 적기
#     end_index = len(money) - 1
    
#     while True:
#         max_index = money.index(max(money))
#         if money[max_index] <= 0:
#             break
#         answer += money[max_index]
#         if max_index == end_index:
#             money[max_index-1], money[max_index], money[0] = 0, 0, 0
#         else:
#             money[max_index-1], money[max_index], money[max_index+1] = 0, 0, 0
#     return answer