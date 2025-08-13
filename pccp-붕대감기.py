def solution(bandage, health, attacks):
    answer = health
    before_attack = attacks[0][0]
    for i in attacks:
        if(i[0] - before_attack >bandage[0]):
            x = (i[0]-before_attack-1) //(bandage[0])
            for j in range(int(x)):

                answer+=bandage[2]
        y = i[0]-before_attack-1

        for k in range(y):
            answer += bandage[1]

        answer -= i[1]
        before_attack = i[0]
        print(answer)
    
    if(answer<0):
        return -1
    return answer   


a = solution(	[5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])

print(a)