def solution(cacheSize, cities):
    answer = 0
    for i in range(len(cities)):
        cities[i] = cities[i].upper()

    a = []

    for i in range(cacheSize):
        a.append(cities[i])
        answer+=5

    idx = 0
    for i in range(cacheSize, len(cities)):
        print(a)
        check = 0
        for j in range(len(a)):
            if(cities[i] == a[j]):
                check = 1
                for k in range(j,len(a)-2):
                    a[k] = a[k+1]
                a[len(a)-1] = cities[i]
        
        if(check == 1):
            answer+=1
        else:
            answer+=5
            
            for l in range(len(a)-2):
                a[l] = a[l+1]
            
            a[len(a)-1] = cities[i]




    return answer


print(solution(3, 		["Jeju", "Pangyo", "NewYork", "newyork"]))