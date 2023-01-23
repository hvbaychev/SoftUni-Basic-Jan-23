minutes_control = int(input())
seconds_contol = int(input())
length_chute = float(input())
second_for_hundred_meters = int(input())


total_for_controls = (minutes_control * 60) + seconds_contol

resistance = length_chute / 120
total_resistance = resistance * 2.5

total_time = (length_chute / 100) * second_for_hundred_meters - total_resistance

if total_for_controls >= total_time:
    print('Marin Bangiev won an Olympic quota!')
    print(f"His time is {total_time:.3f}.")
else:
    total_time = abs(total_for_controls - total_time)
    print(f"No, Marin failed! He was {total_time:.3f} second slower.")

