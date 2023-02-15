capacity = float(input())
counter_day = 0
total_volume = 0
counnter = 0
while True:
    volume = input()
    if volume == 'End':
        break

    volume_int = float(volume)
    if total_volume + volume_int > capacity:
        break
    counnter += 1
    counter_day += 1

    if counter_day == 3:
        total_volume += volume_int * 1.10
        counter_day = 0
    else:
        total_volume += volume_int

if volume == 'End':
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {counnter} suitcases loaded.")
else:
    print("No more space!")
    print(f"Statistic: {counnter} suitcases loaded.")