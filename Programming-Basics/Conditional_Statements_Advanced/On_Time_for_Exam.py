exam_hours = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
total_exam = exam_hours * 60 + exam_minute
total_arrival = arrival_hour * 60 + arrival_minute
if total_exam == total_arrival:
    print("On time")
elif total_exam > total_arrival:
    diff = total_exam - total_arrival
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        diff_hour = diff // 60
        diff_mins = diff % 60
        if diff_mins < 10:
            print("Early")
            print(f"{diff_hour}:0{diff_mins} hours before the start")
        else:
            print("Early")
            print(f"{diff_hour}:{diff_mins} hours before the start")
    elif 30 < diff <= 60:
        diff_mins = diff % 60
        print("Early")
        print(f"{diff_mins} minutes before the start")
elif total_exam < total_arrival:
    diff = total_arrival - total_exam
    if diff < 60:
        print("Late")
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        diff_hour = diff // 60
        diff_mins = diff % 60
        if diff_mins < 10:
            print("Late")
            print(f"{diff_hour}:0{diff_mins} hours after the start")
        else:
            print("Late")
            print(f"{diff_hour}:{diff_mins} hours after the start")
