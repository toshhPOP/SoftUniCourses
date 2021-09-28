balls = int(input())
best_score = 0
best_snow = 0
best_time = 0
best_quality = 0
for i in range(1, balls + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_score = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_score > best_score:
        best_score = snowball_score
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_snow} : {best_time} = {int(best_score)} ({best_quality})")