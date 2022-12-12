def solution(n, arr1, arr2):
    total = []
    
    for i in range(n):
        total.append(arr1[i] | arr2[i])
    for i in range(n):
        total[i] = str(bin(total[i])[2:])
    for i in range(n): # zfill
        if len(total[i]) < n:
            while len(total[i]) < n:
                total[i] = '0' + total[i]
        
    for i in range(n):
        total[i] = total[i].replace('1', '#')
        total[i] = total[i].replace('0', ' ')
            
    return total