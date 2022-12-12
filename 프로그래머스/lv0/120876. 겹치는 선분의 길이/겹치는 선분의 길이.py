def solution(lines):
    start_list = [line[0] for line in lines]
    end_list = [line[1]  for line in lines]
    line_count = 0
    len = 0
    
    for curr in range(min(start_list), max(end_list)):
        if curr in start_list:
            line_count += start_list.count(curr)
        if curr in end_list:
            line_count -= end_list.count(curr)
        if 1 < line_count:
            len += 1
        curr += 1
    
    return len