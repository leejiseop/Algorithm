def solution(strings, n):
    word_dic = {}
    answer = []
    
    for word in strings:
        if word[n] not in word_dic:
            word_dic[word[n]] = []
        word_dic[word[n]].append(word)
    word_list = list(word_dic.items())
    word_list.sort(key = lambda x:x[0])
    for words in word_list:
        words[1].sort()
        answer.extend(words[1])
        
    return answer