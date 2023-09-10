def solution(n, times):
    left = 1
    right = min(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
     	
        for time in times:
            people += mid // time
            if n <= people:
                break
                
        if n <= people: # case: 'times = [10 12 15], mid = 20'
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    return answer
    #     if total >= n:
    #         end = mid
    #     else:
    #         start = mid + 1
    # answer = start
    # return answer