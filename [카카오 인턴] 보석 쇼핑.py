from collections import defaultdict

def solution(gems):
    answer = [1 , len(gems)]
    counter = defaultdict(int)
    left = 0
    piece = len(set(gems))

    for right,i in enumerate(gems):
        counter[i] += 1
        while(len(counter) == piece):
            if( right - left < answer[1] - answer[0]):
                answer = [left+1, right+1]
            counter[gems[left]] -= 1

            if(counter[gems[left]] == 0):
                del(counter[gems[left]])
            left+=1

    return answer