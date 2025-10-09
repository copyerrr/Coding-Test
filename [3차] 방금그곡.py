def solution(m, musicinfos):
    possible = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for i in musicinfos:
        start, end, name, last = i.split(",")
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        total = (end_h*60+end_m) - (start_h*60+start_m)
        a = b = 0
        music = ''
        last = last.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        while a < total:
            music += last[b]
            b+=1
            if(b == len(last)):
                b = 0
            if( last[b] == "#"):
                continue
            a+=1
        if m in music:
            possible.append([name, total])
        
    if not possible:
        return "(None)"

    possible.sort( key = lambda x : x[1], reverse=True)

    return possible[0][0]