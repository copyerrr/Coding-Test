from collections import deque

def check_same(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            cnt+=1
        if(cnt > 1):
            break
    if(cnt==1):
        return 1

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque([(begin, 0)])
    visited = set([begin])

    while(q):
        word, step = q.popleft()
        
        if (word==target):
            return step
        
        for next_word in words:
            if next_word not in visited and check_same(word, next_word):
                visited.add(next_word)
                q.append((next_word, step + 1))

    return 0