from collections import deque

def solution(orders, course):
    answer = []

    def dfs ( order, start,depth, max_length, cur):
        if depth == max_length:
            sorted_key = ''.join(sorted(cur))
            word_list[sorted_key] = word_list.get(sorted_key, 0) + 1
            return

        for i in range(start, len(order)):
            dfs(order, i+1, depth+1, max_length, cur + order[i])
            
    for i in course:
        word_list = {}
        for j in orders:
            visited = [False] * len(j)
            dfs(j,0,0,i,'')
        many_order = list(word_list.values())
        many_order.sort(reverse = True)

        for idx, i in enumerate(list(word_list.values())):
            if(i == many_order[0] and i != 2):
                answer.append(list(word_list.keys())[idx])
    
    answer.sort()

    return answer