import itertools

def is_decimal(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**1/2) + 1):
        if number % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    p = []
    
    for i in range(1, len(numbers) + 1):
        p += list(itertools.permutations(list(numbers), i))
        
    final_p = set([int(''.join(i)) for i in p])
    
    for num in final_p:
        if is_decimal(num):
            answer += 1
    
    return answer