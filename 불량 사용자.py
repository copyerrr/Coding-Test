def check(word1, word2):

    if (len(word1) != len(word2)):
        return False
    
    for idx,i in enumerate(word2):
        if( i != '*' and word1[idx] != word2[idx] ):
            return False
    
    return True

    

def solution(user_id, banned_id):
    answer = 0
    idx = []
    for i in banned_id:
        possible = []
        for j in user_id:
            if(check(j,i)):
                possible.append(j)
        idx.append(possible)
    
    temp = set()
    def dfs(depth,all_set):
        if( depth == len(idx)):
            temp.add(tuple(sorted(all_set)))
            return
        
        for i in idx[depth]:
            if i not in all_set:
                dfs(depth+1, all_set | {i})

    dfs(0,set())
    return len(temp)

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))