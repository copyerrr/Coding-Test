def solution(video_len, pos, op_start, op_end, commands):

    hour, minutes = map(int, pos.split(":"))
    video_hour, video_minutes = map(int, video_len.split(":"))
    ops_hour, ops_minutes = map(int, op_start.split(":"))
    ope_hour, ope_minutes = map(int, op_end.split(":"))

    if (ops_hour, ops_minutes) <= (hour, minutes) <= (ope_hour, ope_minutes):
        hour = ope_hour
        minutes = ope_minutes
    for i in commands:
        
        if (i == 'next'):
            minutes += 10
            if (minutes >= 60):
                hour += 1
                minutes -= 60
            if (hour > video_hour or (hour == video_hour and minutes > video_minutes)):
                hour = video_hour
                minutes = video_minutes
        elif (i == 'prev'):
            minutes -= 10
            if (minutes < 0):
                hour -= 1
                minutes += 60
            if (hour < 0):
                hour = 0
                minutes = 0
        if (ops_hour, ops_minutes) <= (hour, minutes) <= (ope_hour, ope_minutes):
            hour = ope_hour
            minutes = ope_minutes

    answer = f'{hour:02d}:{minutes:02d}'
    return answer