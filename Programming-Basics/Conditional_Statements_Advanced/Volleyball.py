import math
year = input()
holidays = int(input())
weekends_home = int(input())
weekends = 48
saturday_play = (weekends - weekends_home)
sunday_play  = weekends - saturday_play
saturday_play *= 3/4
holiday_play = holidays * 2/3
total_play = sunday_play + saturday_play + holiday_play
if year == "leap":
    total_play += total_play*0.15
print(math.floor(total_play))