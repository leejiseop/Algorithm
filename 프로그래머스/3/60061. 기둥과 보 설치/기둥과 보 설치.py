def is_ok(answer):
    for i in answer:
        x, y, a = i
        if a == 0: # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    
    for x, y, stuff, op in build_frame:
        if op == 0: # 삭제
            answer.remove([x, y, stuff])
            if not is_ok(answer):
                answer.append([x, y, stuff])
        if op == 1: # 설치
            answer.append([x, y, stuff])
            if not is_ok(answer):
                answer.remove([x, y, stuff])
                    
    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    
    return answer