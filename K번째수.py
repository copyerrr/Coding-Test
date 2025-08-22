def solution(array, commands):
    answer = []
    for i in commands:
        sliced_array = array[i[0]-1 : i[1]]
        sort_arr = sorted(sliced_array)
        answer.append(sort_arr[i[2]-1])

    return answer