budjet = int(input())
season = input()
fishers = int(input())

spring_rent = 3000
leten_rent = 4200
winter = 2600

money = 0

if season == 'Summer' or 'Autumn':
    money = leten_rent
    if 0 <= fishers <= 6:
        money *= 0.90
    elif 7 <= fishers <= 11:
        money *= 0.85
    elif fishers >= 12:
        money *= 0.75


if season == 'Spring':
    money = spring_rent
    if 0 <= fishers <= 6:
        money *= 0.90
    elif 7 <= fishers <= 11:
        money *= 0.85
    elif fishers >= 12:
        money *= 0.75


if season == 'Winter':
    money = winter
    if 0 <= fishers <= 6:
        money *= 0.90
    elif 7 <= fishers <= 11:
        money *= 0.85
    elif fishers >= 12:
        money *= 0.75

if season != 'Autumn' and fishers % 2 == 0:
    money = money * 0.95

remain = abs(money - budjet)

if budjet >= money:
    print(f'Yes! You have {remain:.2f} leva left.')
else:
    print(f'Not enough money! You need {remain:.2f} leva.')