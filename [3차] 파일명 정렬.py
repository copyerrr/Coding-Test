def solution(files):
    answer = []

    file_name = []
    for i in files:
        number = 0
        name = ""
        tail = ""
        cnt = 0
        start = 0
        for j in range(len(i)):
            if( i[j] == "0" and start == 0):
                cnt+=1
            elif( "1" <= i[j] <= "9"  and start == 0):
                cur = int(i[j])
                number+= cur
                start = 1
            elif( "0" <= i[j] <= "9"  and start == 1 ):
                number*= 10
                cur = int(i[j])
                number+= cur
            else:
                if(start == 0):
                    name += i[j]
                else:
                    tail += i[j]
        
        number = str(number)
        for i in range(cnt):
            number = "0" + number
        file_name.append([name,number,tail])
    
    file_name.sort( key = lambda x : (x[0].lower(), int(x[1])))

    for i in file_name:
        final = i[0] + i[1] + i[2]
        answer.append(final)
                

    return answer

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"] ))


# head 사전순 대소문자 구분 x
# number 순으로 정렬 9 < 10 < 0011 < 012 ....
# 