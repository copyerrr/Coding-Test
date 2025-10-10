def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        prev = s[0:i]
        cnt = 1
        string = ""
        for j in range(i,len(s),i):
            cur = s[j:j+i]

            if prev == cur:
                cnt+=1
            else:
                if(cnt>=2):
                    string += str(cnt)
                string += prev

                prev = cur
                cnt = 1
        if cnt>=2:
            string+= str(cnt)
        string+=prev
        
        answer = min(answer, len(string))

    
    return answer


print(solution("abcabcabcabcdededededede"))