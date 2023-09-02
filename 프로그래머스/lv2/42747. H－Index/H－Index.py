def solution(citations):
    H_Index = 0
    
    citations.sort(reverse = True)
    
    while all(H_Index <= i for i in citations[:H_Index]) and H_Index == len(citations[:H_Index]):
        H_Index += 1
    
    return H_Index - 1


# def solution(citations):
#     citations.sort(reverse=True)
#     h_index = 0
#     for c in citations:
#         if c > h_index:
#             h_index += 1
#     return h_index