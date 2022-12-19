def solution(x):
    list_x = [int(a) for a in str(x)]
    num_sum = sum(list_x)
    if x % num_sum == 0:
        return True
    return False