from collections import deque

def bfs(start, graph, visited):

    q = deque([start])
    visited[start] = True

    while(q):
        a = q.popleft()
        for b in range(len(graph)):
            if(graph[a][b] == 1 and visited[b] != True):
                visited[b] = True
                q.append(b)

def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i in range(n):
        if(visited[i] != True):
            bfs(i,computers,visited)
            answer+=1

    return answer