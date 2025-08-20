def solution(progresses, speeds):
    answer = []
    i = 0
    
    n = len(progresses)
    while( i < n):
        a=0
        for j in range(len(progresses)):
            progresses[j] += speeds[j]
        while(progresses and progresses[0] >= 100):
            del(progresses[0])
            del(speeds[0])
            a+=1  
            i+=1
        if(a>0):
            answer.append(a)  
    return answer


a = solution ( [93, 30, 55],	[1, 30, 5] )
print(a)