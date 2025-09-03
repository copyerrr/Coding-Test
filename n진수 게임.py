def solution(n, t, m, p):
    answer = ''

    def jinsu(num,  n):
        x = []
        if(num==0):
            x.append(0)
        while(num>0):
            x.append(num%n) 
            num //= n
        x.reverse()
        for i in range(len(x)):
            if(10<=x[i]<=15):
                if(x[i] == 10):
                    x[i]='A'
                if(x[i] == 11):
                    x[i]='B'
                if(x[i] == 12):
                    x[i]='C'
                if(x[i] == 13):
                    x[i]='D'
                if(x[i] == 14):
                    x[i]='E'
                if(x[i] == 15):
                    x[i]='F'
        for i in range(len(x)):
            x[i] = str(x[i])
        return x
    
    number = 0
    cnt = 1
    while(len(answer) < t):
        a = jinsu(number,n)
        for j in a:
            if(cnt% m == p%m):
                answer+= j
                if(len(answer) == t):
                    break
                cnt+=1
            else:
                cnt+=1
        number+=1
        

    return answer