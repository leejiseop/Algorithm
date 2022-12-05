def get_gradient(first, second):
    # if first[0] == second[0]:
    #     return "vertical"
    if first[1] == second[1]:
        return "horizontal"
    gradient = (first[1] - second[1]) / (first[0] - second[0])
    return gradient

def solution(dots):
    if (get_gradient(dots[0], dots[1]) == get_gradient(dots[2], dots[3]) or
        get_gradient(dots[0], dots[2]) == get_gradient(dots[1], dots[3]) or
        get_gradient(dots[0], dots[3]) == get_gradient(dots[1], dots[2])):
        return 1
    return 0