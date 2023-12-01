def solution(s):
    result = 0
    length = len(s)
    answer = length
    half = length // 2
    
    for word in range(1, half + 1):
        result = 0
        count = 1
        prev = ''
        for start in range(0, length - word + 1, word):
            curr = s[start : start+word]
            if prev == curr:
                count += 1 # 2, 3, 4, ...
            else:
                if 2 <= count:
                    result += len(prev) + len(str(count)) # 정수 + prev 추가
                    count = 1
                else:
                    result += len(prev) # prev 추가
            prev = curr
        else: # 마지막 처리
            if 2 <= count:
                result += len(curr) + len(str(count)) # 정수 + curr 추가
            elif count == 1:
                result += len(curr) # curr 추가
            result += len(s[start+word : length])
        answer = min(answer, result)
    
    return answer