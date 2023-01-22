n = int(input())
day_or_night = input()

taxi_start = 0.70
taxi_day = 0.79 * n
taxi_day_total = taxi_day + taxi_start
taxi_night = 0.90 * n
taxi_night_total = taxi_night + taxi_start
autobus_price = 0.09 * n
train_price = 0.06 * n

if n < 20 and day_or_night == "day":
    print(f"{taxi_day_total:.2f}")
elif n < 20 and day_or_night == "night":
    print(f"{taxi_night_total:.2f}")
elif 20 <= n < 100:
    print(f"{autobus_price:.2f}")
else:
    print(f"{train_price:.2f}")