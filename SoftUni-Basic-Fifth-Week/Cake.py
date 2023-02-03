size_one = int(input())  # 10
size_two = int(input())  # 10
total_size = size_one * size_two  # 100
no_more = 'True'

command = input()
while command != 'STOP':
    if command == 'STOP':
        break

    command = int(command)
    total_size -= command

    if total_size <= 0:
        no_more = 'False'
        break

    command = input()

if no_more == 'False':
    diff = abs(total_size)
    print(f'No more cake left! You need {diff:.0f} pieces more.')
else:
    print(f'{total_size:.0f} pieces are left.')
