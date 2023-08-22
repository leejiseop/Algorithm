from collections import Counter

def solution(X, Y):
    answer = ''
    cnt_X = Counter(X)
    cnt_Y = Counter(Y)
    final = [0 for i in range(0, 10)]
    for i in range(0, 10):
        final[i] = min(cnt_X[str(i)], cnt_Y[str(i)])
    for i in range(9, -1, -1):
        answer += str(i) * final[i]
        
    if answer == '':
        return '-1'
    if len(answer) == final[0]:
        return '0'
    return answer

#     cnt_X = [0 for i in range(0, 10)]
#     cnt_Y = [0 for i in range(0, 10)]
#     cnt_result = [0 for i in range(0, 10)]
#     answer = []
#     # cnt는 count()를 쓰자.....
#     for d in X:
#         cnt_X[int(d)] += 1
#     for d in Y:
#         cnt_Y[int(d)] += 1
#     for i in range(0, 10):
#         cnt_result[i] = min(cnt_X[i], cnt_Y[i])
        
#     if len(set(cnt_result)) == 1 and cnt_result[0] == 0:
#         return '-1'
#     if len(set(cnt_result)) == 2 and (0 < cnt_result[0] and cnt_result[1] == 0):
#         return '0'
    
#     for i in range(0, 10):
#         answer.append(str(i)*cnt_result[i])
#     answer.sort(reverse = True)
    
#     return ''.join(answer)