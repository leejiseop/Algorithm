def solution(sizes):
    
    for size in sizes:
        size.sort()
        
    w = max(sizes, key = lambda x: x[0])[0]
    h = max(sizes, key = lambda x: x[1])[1]
        
    return w * h

# 기존 풀이
# def solution(sizes):
#     answer = 0
#     max_w, max_h = 0, 0
#     for i in range(0, len(sizes)):
#         first = max(max_w, sizes[i][0]) * max(max_h, sizes[i][1])
#         second = max(max_w, sizes[i][1]) * max(max_h, sizes[i][0])
#         if first <= second:
#             max_w = max(max_w, sizes[i][0])
#             max_h = max(max_h, sizes[i][1])
#         else:
#             max_w = max(max_w, sizes[i][1])
#             max_h = max(max_h, sizes[i][0])
#     return max_w * max_h