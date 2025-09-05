def solution(k, dungeons):
    answer = -1

    visited = [False] * len(dungeons)

    def dfs(k, depth, max_depth):
        
        if(depth > max_depth):
            max_depth = depth
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                if(dfs(k-dungeons[i][1], depth+1, max_depth) > max_depth):
                    max_depth = dfs(k-dungeons[i][1], depth+1, max_depth)
                visited[i] = False
        return max_depth
            
    answer = dfs(k,0,0)

    return answer