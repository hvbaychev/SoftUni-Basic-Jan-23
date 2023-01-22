hour_init = int(input())
minutes_init = int(input())

total_minutes = (hour_init * 60) + minutes_init + 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours > 23:
    hours = 0

if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")