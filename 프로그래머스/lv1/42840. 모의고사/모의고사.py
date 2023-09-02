def solution(answers):
    best = []
    supo1_answer = [1, 2, 3, 4, 5]
    supo2_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo1 = [0, 1]
    supo2 = [0, 2]
    supo3 = [0, 3]
    
    for i, answer in enumerate(answers):
        if supo1_answer[(i % 5)] == answer:
            supo1[0] += 1
        if supo2_answer[(i % 8)] == answer:
            supo2[0] += 1
        if supo3_answer[(i % 10)] == answer:
            supo3[0] += 1

    if max(supo1[0], supo2[0], supo3[0]) == supo1[0]:
        best.append(supo1[1])
    if max(supo1[0], supo2[0], supo3[0]) == supo2[0]:
        best.append(supo2[1])
    if max(supo1[0], supo2[0], supo3[0]) == supo3[0]:
        best.append(supo3[1])
            
    return best