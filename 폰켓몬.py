from collections import *

def solution(nums):
    answer = 0
    Counter_nums = Counter(nums)
    
    a = len(Counter_nums.values())

    if a> len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = a

    return answer

b = solution([3, 1, 2, 3])
print(b)