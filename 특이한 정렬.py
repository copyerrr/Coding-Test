def solution(numlist, n):
    answer = []
    x = []
    for i in numlist:
        x.append(( abs(i-n) , -i))
        
    x.sort()
    for i in x:
        answer.append(abs(i[1]))
    return answer


print(solution([1, 2, 3, 4, 5, 6],	4))