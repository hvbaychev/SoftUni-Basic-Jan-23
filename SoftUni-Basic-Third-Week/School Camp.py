season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
first_sum = 0
sport = ''

if group in ('boys', 'girls'):
    if season == 'Winter':
        price = 9.60
    elif season == 'Spring':
        price = 7.20
    elif season == 'Summer':
        price = 15

if group == 'mixed':
    if season == 'Winter':
        price = 10
    elif season == 'Spring':
        price = 9.50
    elif season == 'Summer':
        price = 20

first_sum = (price * nights) * students

if students >= 50:
    first_sum = first_sum * 0.50
elif 20 <= students < 50:
    first_sum = first_sum * 0.85
elif 10 <= students < 20:
    first_sum = first_sum * 0.95

if group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'

if group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'

if group == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'

print(f'{sport} {first_sum:.2f} lv.')
