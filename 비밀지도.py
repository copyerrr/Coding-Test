def solution(n, arr1, arr2):
    answer = []

    for x,y in zip(arr1,arr2):
        a = format(x | y, 'b').zfill(n)
        answer.append(a.replace('1','#').replace('0',' '))

    return answer


print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))