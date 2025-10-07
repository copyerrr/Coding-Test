from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2

    if( total % 2 != 0):
        return -1
    
    goal = total//2

    max_try = len(queue1) * 3

    while sum1 != goal:
        if answer>=max_try:
            return -1
        
        if sum1>goal:
            a = q1.popleft()
            q2.append(a)
            sum1 -= a
            sum2 += a
        else:
            b = q2.popleft()
            q1.append(b)
            sum1 += b
            sum2 -= b
        answer +=1


    return answer