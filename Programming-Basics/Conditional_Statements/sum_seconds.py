import math
time_first = int(input())
time_second = int(input())
time_third = int(input())
total_seconds = time_first + time_second + time_third
mins = total_seconds / 60
secs = total_seconds % 60
mins = math.floor(mins)
if secs < 10:
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")