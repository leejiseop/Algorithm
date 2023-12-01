def solution(s):
    result = 0
    length = len(s)
    answer = length
    half = length // 2
    
    for word in range(1, half + 1):
        # print(str(word) + ' size try *********************************')
        result = 0
        count = 1
        prev = ''
        for start in range(0, length - word + 1, word):
            curr = s[start : start+word]
            # print('curr : ' + curr)
            # print('prev : ' + prev)
            # print('prev_count : ' + str(count))
            if prev == curr:
                count += 1 # 2, 3, 4, ...
                # print('prev_count_update : ' + str(count))
            else:
                if 2 <= count:
                    result += len(prev) + len(str(count)) # 정수 + prev 추가
                    # print(str(count) + prev)
                    count = 1
                else:
                    result += len(prev) # prev 추가
                    # print(prev)
            prev = curr
        else:
            if 2 <= count:
                result += len(curr) + len(str(count)) # 정수 + curr 추가
                # print(str(count) + curr)
            elif count == 1:
                result += len(curr) # curr 추가
            # print('last : ' + s[start+word : length])
            result += len(s[start+word : length])
            # print(result)
        answer = min(answer, result)
        # print('==========')
    
    return answer