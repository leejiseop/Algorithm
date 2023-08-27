def find_start(park, len_x, len_y):
    for i in range(0, len_x):
        for j in range(0, len_y):
            if park[i][j] == 'S':
                return [i, j]
    return [-1, -1]

def solution(park, routes):
    answer = []
    len_x = len(park)
    len_y = len(park[0])
    dog = find_start(park, len_x, len_y)
    for route in routes:
        route_info = route.split(' ')
        here = dog.copy()
        
        for i in range(0, int(route_info[1])):
            if route_info[0] == 'N':
                here[0] -= 1
            elif route_info[0] == 'S':
                here[0] += 1
            elif route_info[0] == 'W':
                here[1] -= 1
            elif route_info[0] == 'E':
                here[1] += 1
                
            if here[0] < 0 or here[1] < 0:
                break
            if len_x <= here[0] or len_y <= here[1]:
                break
            if park[here[0]][here[1]] == 'X':
                break

#         if here[0] < 0 or here[1] < 0:
#             continue
#         if len_x <= here[0] or len_y <= here[1]:
#             continue
#         if park[here[0]][here[1]] == 'X':
#             continue
        
#          dog = here.copy()
        else:
            dog = here.copy()



    
    return dog