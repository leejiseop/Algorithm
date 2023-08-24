def solution(board, moves):
    answer = 0
    goal = []
    temp = 0
    
    for line in moves:
        for i, here in enumerate(board):
            if here[line - 1] != 0:
                goal.append(here[line - 1])
                here[line - 1] = 0
                if temp == 0:
                    temp = 1
                elif temp == 1 and goal[-1] == goal[-2] :
                    answer += 2
                    goal.pop()
                    goal.pop()
                if not goal:
                    temp = 0
                break
                
    return answer