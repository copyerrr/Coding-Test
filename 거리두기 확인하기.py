from collections import deque

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs(board, row,col):

    q = deque([(row,col,0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[row][col] = True

    while q:
        r ,c ,dist = q.popleft()

        if dist>=2:
            continue

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0 <= nr <5  and 0 <= nc < 5 and not visited[nr][nc]:
                if board[nr][nc] == "P":
                    return False
                elif board[nr][nc] == "O":
                    if dist<2:
                        visited[nr][nc] = True
                        q.append((nr,nc,dist+1))
                elif board[nr][nc] == "X":
                    visited[nr][nc] = True
    return True

def solution(places):
    answer = []
    
    for i in places:
        check = 1
        temp = []
        for x, j in enumerate(i):
            for y,k in enumerate(j):
                if(k == "P"):
                    temp.append([x,y])
        for r, c in temp:
            if not bfs(i,r,c):
                answer.append(0)
                check = 0
                break
        if(check == 1):
            answer.append(1)

            

    return answer