def solution(n, t, m, timetable):
    
    crew_arrival = []
    for time_str in timetable:
        H, M = map(int, time_str.split(":"))
        crew_arrival.append(H * 60 + M)
    
    crew_arrival.sort()
    
    bus_times = []
    start_time = 9 * 60 
    for i in range(n):
        bus_times.append(start_time + t * i)
        
    last_on_board = -1 
    
    for i, bus_time in enumerate(bus_times):
        current_bus_boarders = []
        
        j = 0
        while j < len(crew_arrival):
            crew_time = crew_arrival[j]
            
            if crew_time <= bus_time and len(current_bus_boarders) < m:
                current_bus_boarders.append(crew_time)
                j += 1
            else:
                break
        
        crew_arrival = crew_arrival[j:]
        if i == n - 1:
            if len(current_bus_boarders) < m:
                last_on_board = bus_time
            else:
                last_crew_time = current_bus_boarders[-1]
                last_on_board = last_crew_time - 1

    final_H = last_on_board // 60
    final_M = last_on_board % 60
    
    return f"{final_H:02d}:{final_M:02d}"


print(solution(	10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))