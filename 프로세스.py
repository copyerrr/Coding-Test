def solution(priorities, location):
    answer = 0
    a = sorted(priorities, reverse=True)

    current = 0
    cnt =1
    for i in a:
        
        for j in priorities[current:] + priorities[:current-1]:
            if(current >= len(priorities)):
                current = 0
            if(i==j):
                if(current == location):
                    return cnt
                current+=1
                break
            current+=1
            
        cnt += 1