def solution(s):
    temp = 0
    
    for c in s:
        if c == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            break
            
    if temp == 0:
        return True
    else:
        return False