size_eggs = input()
color_eggs = input()
count_eggs = int(input())

total_sum = 0
price = 0
remain_money = 0

if size_eggs == 'Large':
    if color_eggs == 'Red':
        price = 16
    elif color_eggs == 'Green':
        price = 12
    elif color_eggs == 'Yellow':
        price = 9

if size_eggs == 'Medium':
    if color_eggs == 'Red':
        price = 13
    elif color_eggs == 'Green':
        price = 9
    elif color_eggs == 'Yellow':
        price = 7

if size_eggs == 'Small':
    if color_eggs == 'Red':
        price = 9
    elif color_eggs == 'Green':
        price = 8
    elif color_eggs == 'Yellow':
        price = 5

total_sum = price * count_eggs
expenses = total_sum * 0.35

remain_money = abs(total_sum - expenses)

print(f'{remain_money:.2f} leva.')