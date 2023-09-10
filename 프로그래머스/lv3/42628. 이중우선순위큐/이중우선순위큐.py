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
                h.remove(max(h)) # remove 이후 다시 heapify가 필요하다! heap이 깨짐..
            elif h and int(temp[1]) == -1:
                heapq.heappop(h)
    if h:
        return [max(h), min(h)]
    else:
        return [0, 0]

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