# 10:05
def solution(friends, gifts):
    f_num = len(friends)
    
    answer = [0] * f_num
    graph = [ [0] * f_num for _ in range(f_num)]
    
    f_dic = {}
    f_answer = {}
    
    for i in range(f_num):
        f_dic[friends[i]] = i
        f_answer[friends[i]] = 0
        
    for gift in gifts:
        fr, to = gift.split()
        fr_i = f_dic[fr]
        to_i = f_dic[to]
        graph[fr_i][to_i] += 1
        
    result = [ [0] * 3 for _ in range(f_num)]
    
    for i in range(f_num):
        give = sum(graph[i])
        get = sum([ line[i] for line in graph])
        result[i] = [give, get, (give - get)]
        
    for a in range(f_num):
        for b in range(f_num):
            if a == b or graph[a][b] == 987654321:
                continue
            if graph[a][b] != 0 or graph[b][a] != 0:
                if graph[a][b] < graph[b][a]:
                    answer[b] += 1
                elif graph[b][a] < graph[a][b]:
                    answer[a] += 1
            if graph[a][b] == graph[b][a]:
                if result[a][2] < result[b][2]:
                    answer[b] += 1
                elif result[b][2] < result[a][2]:
                    answer[a] += 1
            graph[a][b] == 987654321
            graph[b][a] = 987654321
            
    return max(answer)