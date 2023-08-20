def solution(nums):
    mon_set = set(nums)
    diverse = len(mon_set)
    half_nums = len(nums) // 2
    
    return min(half_nums, diverse)