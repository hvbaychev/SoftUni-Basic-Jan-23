import math

record_in_sec = float(input())
distance_in_meter = float(input())
time_in_sec_swim = float(input())

distance_swim = distance_in_meter * time_in_sec_swim

resistance_swim = math.floor(distance_in_meter / 15)
total_resistance = (resistance_swim * 12.5)

total_time_swim = distance_swim + total_resistance

if record_in_sec <= total_time_swim:
    more_need_time = abs(record_in_sec - total_time_swim)
    print(f'No, he failed! He was {more_need_time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time_swim:.2f} seconds.')
