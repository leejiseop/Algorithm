def solution(s):
    answer = ""
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    word = ""
    
    for c in s:
        if c.isnumeric():
            answer += c
            continue
            
        word += c
        
        if word in dic:
            answer += dic[word]
            word = ""
            continue
    
    return int(answer)