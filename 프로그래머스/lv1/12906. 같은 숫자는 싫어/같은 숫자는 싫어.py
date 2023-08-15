def solution(arr):
    answer = []
    answer.append(arr[0])
    len_arr = len(arr)
    
    if len_arr == 1:
        return answer
    
    for i in range(1, len_arr):
        if arr[i - 1] != arr[i]:
            answer.append(arr[i])
    
    return answer