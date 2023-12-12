#1:47
import sys
sys.setrecursionlimit(10**7)

def cut(string):
    op = 0
    cl = 0
    length = len(string)
    cut_index = length - 1
    for i in range(length):
        if string[i] == '(':
            op += 1
        if string[i] == ')':
            cl += 1
        if op == cl:
            cut_index = i + 1
            break
    return string[:cut_index], string[cut_index:]

def is_correct(b):
    result = 0
    for c in b:
        if c == '(':
            result += 1
        if c == ')':
            result -= 1
        if result < 0:
            return False
    return True

def rec(w):
    if w == '':
        return ''
    u, v = cut(w)
    if is_correct(u):
        return u + rec(v)
    else:
        make = '('
        make += rec(v)
        make += ')'
        u = u[1:-1]
        for c in u:
            if c == '(':
                make += ')'
            if c == ')':
                make += '('
        return make
    

def solution(p): # 2 <= p <= 1000, even
    return rec(p)