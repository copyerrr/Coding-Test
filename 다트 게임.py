def solution(dartResult):
    answer = 0
    i = 0
    calc = []
    while(i != len(dartResult)):
        if('0' <= dartResult[i] <= '9'):
            if(dartResult[i] == '1' and dartResult[i+1] == '0'):
                num=10
                i+=1
            else:
                num = int(dartResult[i])
        
        if(dartResult[i] == 'D'):
            num = num**2
        elif(dartResult[i] == 'T'):
            num = num **3
        elif(dartResult[i] == '#'):
            num = num* -1
        elif(dartResult[i] == '*'):
            num *= 2
            if(len(calc)>=1):
                calc[len(calc)-1]*=2

        if(i+1 >= len(dartResult) or '0' <= dartResult[i+1] <= '9'):
            calc.append(num)
        i+=1
    print(calc)
    answer= sum(calc)
    return answer