def solution(s):
    answer = 0

    alpha = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    num  = [0,1,2,3,4,5,6,7,8,9]
    a = ''
    
    for i in range(len(s)):
        if(s[i] >= '0' and s[i]<= '9'):
            answer *= 10
            answer += (int(s[i]))
        else:
            a+=s[i]
        for j in range(len(alpha)):
            if(a==alpha[j]):
                a = ''
                answer *= 10
                answer += int(num[j])
    
    
    return answer