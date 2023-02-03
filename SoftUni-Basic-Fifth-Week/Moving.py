free_space = int(input())
length_space = int(input())
tall_space = int(input())
total_space = free_space * length_space * tall_space

sum_box = 0

command = input()
while total_space >= sum_box:
    if command == 'Done':
        diff = abs(total_space - sum_box)
        if total_space > sum_box:
            print(f'{diff} Cubic meters left.')
        elif total_space <= sum_box:
            print(f'No more free space! You need {diff} Cubic meters more.')
        break

    box_number = int(command)

    sum_box += box_number

    if total_space <= sum_box:
        diff = abs(total_space - sum_box)
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
    command = input()

