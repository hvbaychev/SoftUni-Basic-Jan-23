season = input()
kilometer = float(input())

price_per_km = 0
total_sum = 0
taxes = 0.90
one_season = 4

if kilometer <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.90
    elif season == 'Winter':
        price_per_km = 1.05

if 5000 < kilometer <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.10
    elif season == 'Winter':
        price_per_km = 1.25

if 10000 < kilometer <= 20000:
    if season in ('Spring', 'Autumn', 'Summer', 'Winter'):
        price_per_km = 1.45

total_sum = (price_per_km * kilometer) * one_season

total_sum = total_sum * taxes

print(f'{total_sum:.2f}')