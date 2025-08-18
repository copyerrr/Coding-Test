from collections import *

def solution(participant, completion):
    
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

a = solution(["leo", "kiki", "eden"], ["eden", "kiki"])

print(a)
    