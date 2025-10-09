def is_right(p):
    stack = []

    for i in p:
        if( i == "("):
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
        

def solution(p):

    if not p:
        return ""

    balance = 0
    u, v ="",""
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if is_right(u):
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('

    return answer