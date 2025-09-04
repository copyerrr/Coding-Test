def solution(msg):
    answer = []

    add_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    idx = 27
    i = 0


    while(i != len(msg)):
        found = False
        for j in range(i+1, len(msg)):
            current = msg[i:j]


            if(current+msg[j] not in add_dict):
                add_dict[current+msg[j]] = idx
                idx+=1
                answer.append(add_dict[current])
                i += len(current)
                found = True
                break
        if not found:
            answer.append(add_dict[msg[i:]])
            break
    return answer