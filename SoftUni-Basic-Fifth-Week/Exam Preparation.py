number_wrong_task = int(input())
total_sum = 0
average = 0
number_task = 0
fail = 0
last_name = ''

while True:

    task = input()
    if task == 'Enough':
        break
    evaluation = int(input())
    number_task += 1
    total_sum += evaluation
    last_name = task
    if 2 <= evaluation <= 4:
        fail += 1
    if fail == number_wrong_task:
        break

average = total_sum / number_task
if task == 'Enough':
    task = last_name
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {number_task:.0f}')
    print(f'Last problem: {task}')
else:
    print(f'You need a break, {fail} poor grades.')
