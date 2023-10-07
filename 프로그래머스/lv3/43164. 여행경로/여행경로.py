def solution(tickets):
    answer = []
    total = len(tickets)
    tickets.sort(key = lambda x: (x[0], x[1]))
    v = [False for _ in range(total)]
    print(tickets)
    print(answer)
    
    def dfs(now):
        print('g')
        
        if len(answer) == total + 1:
            return
        
        for i in range(total):
            if tickets[i][0] == now and v[i] == False:
                answer.append(tickets[i][1])
                v[i] = True
                dfs(tickets[i][1])
                if len(answer) == total + 1:
                    return
                v[i] = False
                answer.pop()
        
    answer.append('ICN')
    dfs('ICN')
    
    return answer