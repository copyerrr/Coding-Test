from collections import deque

def solution(stones, k):
    q = deque()
    max_arr = []

    for i, stone in enumerate(stones):
        while q and q[-1][0] < stone:
            q.pop()
        q.append((stone, i))

        if q[0][1] <= i - k:
            q.popleft()

        if i >= k - 1:
            max_arr.append(q[0][0])
        
        print(q)

    return max_arr

    return min(max_arr)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3))