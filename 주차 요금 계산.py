def solution(fees, records):
    answer = []
    
    parking = []

    for i in records:
        a, b, c = i.split(" ")
        hour, minutes = (a.split(":"))
        hour, minutes = int(hour), int(minutes)
        real_time = hour*60 + minutes
        if( c=="IN" ):
            check = 0
            for i in range(len(parking)):
                if b in parking[i][1]:
                    parking[i][0] = real_time
                    parking[i][3] = "IN"
                    check = 1
            if(check ==0):
                parking.append( [real_time, b, 0, "IN"] )
        
        if( c=="OUT" ):
            for i in range(len(parking)):
                if b in parking[i][1]:
                    parking[i][2] += real_time - parking[i][0]
                    parking[i][3] = "OUT"
    
    
    for i in parking:
        if( i[3] == "IN") :
            force = 23*60 + 59
            i[2] += force - i[0]
    parking.sort( key = lambda x : x[1] )

    for i in parking:
        answer.append(i[2])
        
    for idx,i in enumerate(answer):
        if (i - fees[0] > 0 ):
            answer[idx] = fees[1] + (i - fees[0])//fees[2] * fees[3]
            if( (i - fees[0]) % fees[2] > 0):
                answer[idx] += fees[3]
        else:
            answer[idx] = fees[1]
                

    return answer