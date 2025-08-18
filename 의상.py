from collections import *

def solution(clothes):
    answer = 1
    sort_cloth = []
    for i in clothes:
        sort_cloth.append(i[1])
        
    a = Counter(sort_cloth)
    
    for i in list(a.values()):
        answer*= i+1

    return answer-1