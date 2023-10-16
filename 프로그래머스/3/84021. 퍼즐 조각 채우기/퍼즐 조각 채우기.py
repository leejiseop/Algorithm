from collections import deque

def bfs(field, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    lst = []
    length = len(field)
    
    for i in range(length):
        for j in range(length):
            if field[i][j] == num:
                field[i][j] = 5
                q = deque([(i, j)])
                temp = [(i, j)]
                
                while q:
                    x, y = q.popleft()
                    for move in range(4):
                        nx = x + dx[move]
                        ny = y + dy[move]
                        if nx < 0 or length - 1 < nx or ny < 0 or length - 1 < ny:
                            continue
                        if field[nx][ny] == num:
                            field[nx][ny] = 5
                            q.append((nx, ny))
                            temp.append((nx, ny))
                lst.append(temp)
                
    return lst

def make_table(block):
    x_list = [point[0] for point in block]
    y_list = [point[1] for point in block]
    
    x_max, x_min = max(x_list), min(x_list)
    y_max, y_min = max(y_list), min(y_list)
    
    col = x_max - x_min + 1
    row = y_max - y_min + 1
    
    table = [[0] * row for _ in range(col)]
    
    for x, y in block:
        x -= x_min
        y -= y_min
        table[x][y] = 1
    
    return table

def rotate(table):
    new = [[0] * len(table) for _ in range(len(table[0]))]
    row = len(table)
    
    for i in range(len(table)):
        for j in range(len(table[0])):
            new[j][row - i - 1] = table[i][j]
    
    return new

def area(table):
    
    
    return 0

def solution(game_board, table):
    answer = 0
    empty_list = bfs(game_board, 0)
    puzzle_list = bfs(table, 1)
    
    for empty in empty_list:
        is_filled = False
        empty_table = make_table(empty)
        
        for puzzle in puzzle_list:
            if is_filled:
                break
            puzzle_table = make_table(puzzle)
            
            for _ in range(4):
                puzzle_table = rotate(puzzle_table)
                if empty_table == puzzle_table:
                    puzzle_list.remove(puzzle)
                    answer += len(puzzle)
                    is_filled = True
                    break
        
    return answer