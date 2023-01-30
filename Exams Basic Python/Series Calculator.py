import math

serial_name = input()
number_season = int(input())
number_episod = int(input())
time_serial = float(input())

adv = time_serial * 0.20
time_serial = time_serial + adv

add_time_spec_episod = number_season * 10

total_time = (number_season * time_serial * number_episod) + add_time_spec_episod

print(f"Total time needed to watch the {serial_name} series is {math.floor(total_time):.0f} minutes.")