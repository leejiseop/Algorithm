def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1):
        y_w = yellow / i
        y_h = i
        if (y_w * 2) + (y_h * 2) + 4 == brown:
            return [y_w + 2, y_h + 2]