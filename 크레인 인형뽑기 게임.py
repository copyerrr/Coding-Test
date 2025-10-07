def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        col = i-1
        for j in range(len(board)):
            if(board[j][col] != 0):
                cur = board[j][col]
                board[j][col] = 0
                
                if basket and basket[-1] == cur:
                    basket.pop()
                    answer+=2
                else:
                    basket.append(cur)
                
                break

    return answer