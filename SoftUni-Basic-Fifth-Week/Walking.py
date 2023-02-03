reach = 10000
total_step = 0

while True:
    command = input()

    if command == 'Going home':
        step_to_home = int(input())
        total_step += step_to_home
        if total_step < reach:
            diff = abs(total_step - reach)
            print(f'{diff} more steps to reach goal.')
        elif total_step > reach:
            total_step = abs(total_step - reach)
            print('Goal reached! Good job!')
            print(f'{total_step:.0f} steps over the goal!')
        elif total_step == reach:
            total_step = total_step - reach
            print('Goal reached! Good job!')
            print(f'{total_step:.0f} steps over the goal!')
        break

    new_command = int(command)
    total_step = total_step + new_command

    if total_step > reach:
        total_step = total_step - reach
        print('Goal reached! Good job!')
        print(f'{total_step:.0f} steps over the goal!')
        break

    if total_step == reach:
        total_step = total_step - reach
        print('Goal reached! Good job!')
        print(f'{total_step:.0f} steps over the goal!')
        break

