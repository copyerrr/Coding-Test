def solution(s):
    answer = True
    
    a = []

    for i in s:
        if( i == '('):
            a.append(i)
        else:
            if(len(a) == 0):
                return False
            a.pop()

    return True


a = solution("()())")
print(a)