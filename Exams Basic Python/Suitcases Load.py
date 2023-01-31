capacity = float(input())
number_of_suitcase = 0
volume_max = 'true'
new_command = 'true'
total_volume = 0

command = input()
while command != 'End':  #true
    if command == 'End':
        new_command = 'false'
        print("Congratulations! All suitcases are loaded!")
        break

    volume = float(command)

    number_of_suitcase += 1
    if number_of_suitcase % 3 == 0:
        volume = volume * 1.10

    total_volume = total_volume + volume

    if capacity < total_volume:
        volume_max = 'false'
        print("No more space!")
        print(f"Statistic: {number_of_suitcase - 1:.0f} suitcases loaded.")
        break

    command = input()

if capacity >= total_volume:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {number_of_suitcase:.0f} suitcases loaded.")
