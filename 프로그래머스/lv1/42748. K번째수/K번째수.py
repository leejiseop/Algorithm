def solution(array, commands):
    answer = []
    
    for num in range(len(commands)):
        i = commands[num][0]
        j = commands[num][1]
        k = commands[num][2]
        answer.append(sorted(array[i - 1:j])[k - 1])
    
    print()
    return answer