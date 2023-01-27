import time

hour = 0
minute = 0
second = 0

while (hour < 24):
    second += 1
    time.sleep(1)

    if (second >= 60):
        second = 0
        minute += 1

    if (minute >= 60):
        minute = 0
        hour += 1

    print(str(hour) + ":" + str(minute) + ":" + str(second))
