import math

record_in_sec = float(input())
distance = float(input())
time_in_sec_for_meter = float(input())


total_time = distance * time_in_sec_for_meter
resistance = math.floor(distance / 50) * 30

total_time = total_time + resistance


if record_in_sec > total_time:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    total_time = abs(total_time - record_in_sec)
    print(f'No! He was {total_time:.2f} seconds slower.')