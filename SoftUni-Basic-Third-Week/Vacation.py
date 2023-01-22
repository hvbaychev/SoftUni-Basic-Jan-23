money = float(input())
season = input()

total_sum = 0
location = ''
place = ''

if money <= 1000:
    place = 'Camp'
elif 1000 < money <= 3000:
    place = 'Hut'
elif money > 3000:
    place = 'Hotel'

if money <= 1000:
    if season == 'Summer':
        total_sum = money * 0.65
        location = 'Alaska'
    elif season == 'Winter':
        total_sum = money * 0.45
        location = 'Morocco'

if 1000 < money <= 3000:
    if season == 'Summer':
        total_sum = money * 0.80
        location = 'Alaska'
    elif season == 'Winter':
        total_sum = money * 0.60
        location = 'Morocco'

if money > 3000:
    if season == 'Summer':
        total_sum = money * 0.90
        location = 'Alaska'
    elif season == 'Winter':
        total_sum = money * 0.90
        location = 'Morocco'


print(f'{location} - {place} - {total_sum:.2f}')