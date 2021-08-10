import math
record_secs = float(input())
distance = float(input())
time_in_secs = float(input())
ivan_time = distance * time_in_secs
delay = distance / 15
ivan_time += math.floor(delay) * 12.5
if ivan_time < record_secs:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    diff = ivan_time - record_secs
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
