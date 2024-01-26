# 2:00

import heapq

def solution(food_times, k):
    answer = -1
    remain_foods = len(food_times)
    cycle = 0
    hq = []
    
    for i in range(remain_foods):
        heapq.heappush(hq, [food_times[i], i + 1])
        
    while hq:
        now = hq[0][0]
        full = (now - cycle) * remain_foods
        if full <= k:
            k -= full
            while hq and hq[0][0] == now:
                heapq.heappop(hq)
                remain_foods -= 1
            cycle = now
        else:
            last = k % remain_foods
            hq.sort(key = lambda x: x[1])
            answer = hq[last][1]
            break
        
    return answer















# import heapq

# def solution(food_times, k):
#     answer = -1
#     h = []
#     length = len(food_times)
#     prev = 0
    
#     for i in range(length):
#         heapq.heappush(h, (food_times[i], i + 1)) # (남은 음식, 번호)
    
#     while h:
#         now = h[0][0]
#         cycle = (now - prev) * length
#         if cycle <= k:
#             while h and h[0][0] == now:
#                 heapq.heappop(h)
#                 length -= 1
#             prev = now
#             k -= cycle
#         else:
#             h.sort(key = lambda x: x[1])
#             answer = h[k % length][1]
#             break
    
#     return answer