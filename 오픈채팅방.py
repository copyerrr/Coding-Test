def solution(record):
    answer = []

    check_id = []

    for i in record:
        arr = i.split(" ")

        command = arr[0]
        id = arr[1]
        if(command == "Enter" or command == "Change"):
            nickname = arr[2]
            for j in range(len(check_id)):
                if id in check_id[j][1]:
                    check_id[j][2] = nickname
        
        else:
            for j in range(len(check_id)):
                if id in check_id[j][1]:
                    nickname = check_id[j][2]
        check_id.append([command, id, nickname])

        

    for i in check_id:
        if(i[0] == "Enter"):
            answer.append(f"{i[2]}님이 들어왔습니다.")
        elif(i[0] == "Leave"):
            answer.append(f"{i[2]}님이 나갔습니다.")

    
    return answer


print(solution(["Enter uid1 Muzi", "Enter uid12 Prodo", "Change uid1 Ryan"]))