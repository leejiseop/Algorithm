# #1:47 ~ 3:10
# import sys
# sys.setrecursionlimit(10**7)

# def cut(string):
#     op = 0
#     cl = 0
#     length = len(string)
#     cut_index = length - 1
#     for i in range(length):
#         if string[i] == '(':
#             op += 1
#         if string[i] == ')':
#             cl += 1
#         if op == cl:
#             cut_index = i + 1
#             break
#     return string[:cut_index], string[cut_index:]

# def is_correct(b):
#     result = 0
#     for c in b:
#         if c == '(':
#             result += 1
#         if c == ')':
#             result -= 1
#         if result < 0:
#             return False
#     return True

# def rec(w):
#     if w == '':
#         return ''
#     u, v = cut(w)
#     if is_correct(u):
#         return u + rec(v)
#     else:
#         make = '('
#         make += rec(v)
#         make += ')'
#         u = u[1:-1]
#         for c in u:
#             if c == '(':
#                 make += ')'
#             if c == ')':
#                 make += '('
#         return make
    

# def solution(p): # 2 <= p <= 1000, even
#     return rec(p)


# 지렸다
def solution(p):
    if p == '':
        return p
    
    r = True
    c = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if 0 < c: # 닫힌게 더 많으면
            r = False # 올바르지 않다
        if c == 0: # 균형잡혔다면
            if r: # 올바르다면
                return p[:i+1] + solution(p[i+1:])
            else: # 올바르지 않다면
                middle = solution(p[i+1:])
                end = ''.join(list(map(lambda x:'(' if x==')' else ')', p[1:i]) ))
                return '(' + middle + ')' + end
