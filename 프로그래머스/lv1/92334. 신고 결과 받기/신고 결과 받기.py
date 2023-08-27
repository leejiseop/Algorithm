def solution(id_list, report, k):
    answer = []
    # dic 만들어서 set 명단 추가
    id_list_dic = {person: set() for person in id_list}
    for i in report:
        data = i.split(' ')
        id_list_dic[data[1]].add(data[0])
    # id list 돌면서 다른 dic 만들어서 개수 업데이트
    id_list_dic2 = {person: 0 for person in id_list}
    for key, value in id_list_dic.items():
        if k <= len(value):
            for j in value:
                id_list_dic2[j] += 1
    
    return [value for key, value in id_list_dic2.items()]