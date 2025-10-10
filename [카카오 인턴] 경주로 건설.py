from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    N = len(board)
    
    q = deque()
    pay = [[[len(board)**2*600] * N for _ in range(N)] for _ in range(4)]

    if N > 1 and board[0][1] == 0:
        pay[3][0][1] = 100
        q.append((100, 0, 1, 3))
    
    if N > 1 and board[1][0] == 0:
        pay[1][1][0] = 100
        q.append((100, 1, 0, 1))
        
    if N == 1:
        return 0
    
    while q:
        cost, r, c, locate = q.popleft()

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            
            if board[nr][nc] == 1:
                continue
            
            if locate == i:
                new_cost = cost + 100
            else:
                new_cost = cost + 600

            if new_cost < pay[i][nr][nc]:
                pay[i][nr][nc] = new_cost
                q.append((new_cost, nr, nc, i))
    
    return min(pay[d][N-1][N-1] for d in range(4))


def solution(board):
    return bfs(board)