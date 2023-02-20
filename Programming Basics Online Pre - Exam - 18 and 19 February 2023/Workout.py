import math

days = int(input())
kilometers = float(input())
km_per_day = 0
total_km = kilometers

for i in range(1, days+1):
    percent = int(input())
    percent = percent / 100
    daily_percent = kilometers * percent
    km_per_day = kilometers + daily_percent
    total_km += km_per_day
    kilometers = km_per_day


diff = abs(total_km - 1000)
if total_km >= 1000:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")