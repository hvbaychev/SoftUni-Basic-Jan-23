capacity = int(input())
ticket_price = 5
total_sum = 0
sum_people = 0
cinema = 'true'

command = input()
while command != 'Movie time!':
    entrance_people = int(command)
    if sum_people + entrance_people > capacity:
        cinema = 'false'
        break

    sum_people += entrance_people

    total_sum += ticket_price * entrance_people

    if entrance_people % 3 == 0:
        total_sum = total_sum - 5

    command = input()

if cinema == 'false':
    print(f"The cinema is full.\nCinema income - {total_sum:.0f} lv.")
else:
    print(f"There are {capacity - sum_people} seats left in the cinema.\nCinema income - {total_sum:.0f} lv.")