from collections import Counter

def solution(s):
    answer = []

    num = 0
    for i in s:
        
        if( '0' <= i <= '9'):
            num *= 10
            num += int(i)
        elif(num>0):
            answer.append(num)
            num = 0
    
    answer = Counter(answer)

    result = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    ans = []

    for i in result:
        ans.append(i[0])

    return ans




print(solution(  "{{20,111},{111}}" ))