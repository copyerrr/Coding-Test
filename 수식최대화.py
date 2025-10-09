def solution(expression):
    answer = 0

    temp = ''
    idx = []

    for i in expression:
        if not i.isdigit():
            idx.append(temp)
            idx.append(i)
            temp = ''
        else:
            temp += i
    idx.append(temp)

    op = [["*","-","+"] , ["*","+","-"], ["+","-","*"]
          ,["+","*","-"] ,["-","*","+"], ["-","+","*"]]
    
    for i in op:
        temps = idx.copy()
        for j in i:
            stack = []
            k = 0
            while k<len(temps):
                item = temps[k]
                if item == j:
                    left = int(stack.pop())
                    right = int(temps[k+1])

                    if j == "*": stack.append(left * right)
                    elif j == "+" : stack.append(left+right)
                    else : stack.append(left-right)

                    k+=2
                else:
                    stack.append(item)
                    k += 1
            temps = stack
        answer = max(answer,abs(temps[0]))


    return answer