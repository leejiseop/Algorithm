def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left+right)//2
        people = 0
     	
        for time in times:
            people += mid//time
            
            if people >= n:
                break
        if people >= n: # times = [10 12 15], mid = 20
            answer = mid
            right = mid -1
        else :
            left = mid + 1
    return answer