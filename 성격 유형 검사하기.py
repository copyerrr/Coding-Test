def solution(survey, choices):
    answer = ''

    score = { "R" : 0,
             "T" : 0,
              "C" : 0,
               "F" : 0,
                "J" : 0,
                 "M" : 0,
                  "A" : 0,
                   "N" : 0 }

    for idx,i in enumerate(survey):
        a = i[0]
        b = i[1]

        if(choices[idx] == 1):
            score[a] += 3
        elif(choices[idx] == 2):
            score[a] += 2
        elif(choices[idx] == 3):
            score[a] += 1
        elif(choices[idx] == 5):
            score[b] += 1
        elif(choices[idx] == 6):
            score[b] += 2
        elif(choices[idx] == 7):
            score[b] += 3

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]))