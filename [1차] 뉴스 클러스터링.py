def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()

    hap = gyo = 0

    arr1 = []
    arr2 = []
    temp = ''
    i = 0
    while (i<len(str1)):
        if('A' <= str1[i] <= 'Z'):
            temp = temp + str1[i]
        # else:
        #     temp = ''
        
        if(len(temp)== 2):
            arr1.append(temp)
            temp = ''
            i-=1
        i+=1

    temp = ''
    i=0

    while (i<len(str2)):
        if('A' <= str2[i] <= 'Z'):
            temp = temp + str2[i]
        #else:
        #    temp = ''
        
        if(len(temp)== 2):
            arr2.append(temp)
            temp = ''
            i-=1
        i+=1

    print(arr1, arr2)
    hap = len(arr1+arr2)
    for i in arr1:
        for j in arr2:
            if(i==j):
                gyo+=1
                hap-=1

    if(hap==0):
        return 1        

    answer = (gyo*65536//hap)
    
    return answer

print(solution( 	"aa1+aa2", "AAAA12"))