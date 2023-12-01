def rotated(array_2d):
    n = len(array_2d) # 행 길이
    m = len(array_2d[0]) # 열 길이 
    result = [[0] * n for _ in range(m)] # 회전한 결과를 표시하는 배열

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = array_2d[i][j]
    return result


def solution(key, lock): # 02:20
    lock_length, key_length = len(lock), len(key)
    field_length = lock_length + (2 * key_length)
    
    field = [ [0] * field_length for _ in range(field_length)]
    
    for i in range(lock_length):
        for j in range(lock_length):
            field[key_length + i][key_length + j] = lock[i][j]
            
    for i in range(1, lock_length + key_length):
        for j in range(1, lock_length + key_length):
            
            for _ in range(4):
                key = rotated(key)

                for a in range(key_length):
                    for b in range(key_length):
                        field[i + a][j + b] += key[a][b]

                # for g in field:
                #     print(g)
                # print()

                for a in range(lock_length):
                    for b in range(lock_length):
                        # print('field[' + str(i + a) + '][' + str(j + b) + '] = ' + str(field[i + a][j + b]))
                        if field[key_length + a][key_length + b] != 1:
                            # print('qqqqq')
                            break
                    if field[key_length + a][key_length + b] != 1:
                        # print('qqqqq')
                        break
                    # print('ok')
                else:
                    return True

                for a in range(key_length):
                    for b in range(key_length):
                        field[i + a][j + b] -= key[a][b]
            
    return False