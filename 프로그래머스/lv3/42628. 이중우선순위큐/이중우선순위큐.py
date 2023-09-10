import heapq

def solution(operations):
    answer = []
    h = []
    
    for operation in operations:
        temp = operation.split(' ')
        if temp[0] == 'I':
            heapq.heappush(h, int(temp[1]))
        else:
            if h and int(temp[1]) == 1:
                h.remove(max(h))
            elif h and int(temp[1]) == -1:
                heapq.heappop(h)
    if h:
        return [max(h), min(h)]
    else:
        return [0, 0]













# def solution(operations):
#     answer = []
    
#     q = []
#     for operation in operations:
#         x, num = operation.split() 
#         num = int(num)
        
#         if x == 'I':
#             heapq.heappush(q, num)
#         elif x == 'D' and num == 1:
#             if len(q) != 0:
#                 max_value = max(q)
#                 q.remove(max_value)
#         else:
#             if len(q) != 0:
#                 heapq.heappop(q)
    
#     if len(q) == 0:
#         answer = [0, 0]
#     else:
#         answer = [max(q), heapq.heappop(q)]
        
#     return answer




# import heapq

# def solution(operations):
#     heap = []

#     for operation in operations:
#         operator, operand = operation.split(' ')
#         operand = int(operand)

#         if operator == 'I':
#             heapq.heappush(heap, operand)
#         elif heap:
#             if operand < 0:
#                 heapq.heappop(heap)
#             else:
#                 heap.remove(max(heap))

#     if not heap:
#         return [0, 0]

#     return [max(heap), heap[0]]