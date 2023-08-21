def solution(lottos, win_nums):
    low, high = 0, 0
    zero_count, correct_count = 0, 0
    
    for num in lottos:
        if num in win_nums:
            correct_count += 1 # 이럴거면 count 함수를 활용하자!
            win_nums.remove(num)
        if num == 0:
            zero_count += 1
    remain_nums = len(win_nums)
    if remain_nums < zero_count:
        zero_count = remain_nums
        
    low = 7 - correct_count
    high = 7 - (correct_count + zero_count)
    
    if 6 < low:
        low = 6
    if 6 < high:
        high = 6
        
    return [high, low]