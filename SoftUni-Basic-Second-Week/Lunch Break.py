import math

serial_name = str(input())
serial_time = int(input())
break_time = int(input())

time_for_break = break_time * 1 / 8
time_for_relax = break_time * 1 / 4

remain_time = break_time - time_for_break - time_for_relax

if remain_time >= serial_time:
    remain_time_for_rest = abs(serial_time - remain_time)
    remain_time_for_rest = math.ceil(remain_time_for_rest)
    print(f'You have enough time to watch {serial_name} and left with {remain_time_for_rest:.0f} minutes free time.')
else:
    need_time = abs(serial_time - remain_time)
    need_time = math.ceil(need_time)
    print(f"You don't have enough time to watch {serial_name}, you need {need_time} more minutes.")
