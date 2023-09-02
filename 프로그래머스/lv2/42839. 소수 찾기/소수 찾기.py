import itertools

def is_decimal(number):
    if number == 1:
        return False
    
    for i in range(2, int(number**1/2) + 1):
        if number % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    p = []
    for i in range(1, len(numbers) + 1):
        p += list(set(itertools.permutations(list(numbers), i)))
    final_p = [int(''.join(i)) for i in p if i[0] != '0']
    for num in final_p:
        if is_decimal(num):
            answer += 1
    
    # 모든 조합 만들고 set 처리
    # 0으로 시작하는것 빼기
    # 하나씩 전부 소수판별 후 개수 리턴
    
    return answer