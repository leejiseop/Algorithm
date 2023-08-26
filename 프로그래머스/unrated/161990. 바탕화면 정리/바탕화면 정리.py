def solution(wallpaper):
    answer = []
    len_x = len(wallpaper)
    len_y = len(wallpaper[0])
    # x좌표들만 따로 모으로 y좌표들만 따로 모으면 더 편할듯
    # 겹치는 선분의 길이 문제처럼...
    files = []
    
    for x in range(0, len_x):
        for y in range(0, len_y):
            if wallpaper[x][y] == '#':
                files.append([x, y])

    answer.append(min([file[0] for file in files]))
    answer.append(min([file[1] for file in files]))
    answer.append(max([file[0] + 1 for file in files]))
    answer.append(max([file[1] + 1 for file in files]))
    return answer