def solution(numbers):
    answer = 0

    all_num = []
    visited = [False]* len(numbers)

    def dfs(cur):
        if cur:
            all_num.append(int(cur))
        for i in range(len(numbers)):
            if not visited[i]: 
                visited[i] = True
                dfs(cur + numbers[i])
                visited[i] = False
    
    dfs('')
    all_num = set(all_num)
    def sosu(num):
        check = 0
        if(num == 0 or num == 1):
            return 0
        for i in range(2, num//2+1):
            if(num % i == 0):
                
                check = 1
        if(check == 0):
            return 1
    for i in all_num:
        if(sosu(i)):
            answer+=1
    return answer