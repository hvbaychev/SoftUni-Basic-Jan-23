max_floors = int(input())
max_rooms = int(input())


for floor in range(max_floors, 0, -1):
    for room in range(0, max_rooms):
        if floor == max_floors:
            floor_string = 'L'
            print(f'{floor_string}{floor}{room} ', end='')
            if room == max_rooms-1:
                print(' ')

        if floor % 2 == 0 and floor != max_floors:
            floor_string = 'O'
            print(f'{floor_string}{floor}{room} ', end='')
            if room == max_rooms-1:
                print(' ')

        if floor % 2 != 0 and floor != max_floors:
            floor_string = 'A'
            print(f"{floor_string}{floor}{room} ", end='')
            if room == max_rooms-1:
                print(' ')
