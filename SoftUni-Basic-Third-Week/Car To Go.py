money = float(input())
season = input()

total_sum = 0.00
car_type = ''
model_type = ''

if money <= 100:
    car_type = 'Economy class'
elif 100 < money <= 500:
    car_type = 'Compact class'
elif money > 500:
    car_type = 'Luxury class'

if money <= 100:
    if season == 'Summer':
        total_sum = money * 0.35
        model_type = 'Cabrio'
    elif season == 'Winter':
        total_sum = money * 0.65
        model_type = 'Jeep'

if 100 < money <= 500:
    if season == 'Summer':
        total_sum = money * 0.45
        model_type = 'Cabrio'
    elif season == 'Winter':
        total_sum = money * 0.80
        model_type = 'Jeep'

if money > 500:
    if season == 'Summer' or season == 'Winter':
        total_sum = money * 0.90
        model_type = 'Jeep'

print(f'{car_type}')
print(f'{model_type} - {total_sum:.2f}')





