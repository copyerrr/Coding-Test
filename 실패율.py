def solution(N, stages):
    answer = []


    # 2중 for문 시간초과 나는 것 같다 하나 or nlogn 으로 바꿔보자
    cnt = [0 for _ in range(N+1)]
    for i in stages:
        cnt[i-1]+=1

    failure = []
    total = len(stages)
    for i in cnt:
        print(i ,     total)
        failure.append(i/total)
        total-=i

    del(failure[len(failure)-1])

    for idx, i in enumerate(failure):
        failure[idx] = (i, idx+1)

    answer = sorted(failure, key=lambda x: (-x[0], x[1]) )
    last = []
    for i in answer:
        last.append(i[1])
    return last

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))