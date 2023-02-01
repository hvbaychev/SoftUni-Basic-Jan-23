name_player = input()
starting_points = 301
shots = 0
unsuccessful_shots = 0
hit_points = 0

retire_command = 'false'
win_game = 'false'

while True:
    field = input()
    if field == 'Retire':
        retire_command = 'true'
        break
    points = int(input())

    if field == 'Single':
        starting_points -= points
        shots += 1
        hit_points = points
    elif field == 'Double':
        starting_points = starting_points - (points * 2)
        shots += 1
        hit_points = points * 2
    elif field == 'Triple':
        starting_points = starting_points - (points * 3)
        shots += 1
        hit_points = points * 3

    if starting_points < 0:
        shots -= 1
        unsuccessful_shots += 1
        starting_points += hit_points
        continue

    if starting_points == 0:
        win_game = 'true'
        break

if win_game == 'true':
    print(f"{name_player} won the leg with {shots} shots.")
elif retire_command == 'true':
    print(f"{name_player} retired after {unsuccessful_shots} unsuccessful shots.")

