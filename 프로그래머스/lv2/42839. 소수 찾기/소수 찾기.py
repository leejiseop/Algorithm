from itertools import permutations

def checkPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    list_numbers = list(numbers)
    temp = []
    
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(list_numbers, i))
    num = set([int(''.join(i)) for i in temp])
    
    for i in num:
        if checkPrime(i):
            answer += 1
    
    return answer