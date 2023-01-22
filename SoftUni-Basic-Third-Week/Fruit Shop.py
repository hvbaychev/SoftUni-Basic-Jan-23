fruit = input()
day_from_week = input()
quantity = float(input())

price = 0

if day_from_week in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    if fruit == 'banana':
        price = 2.50 * quantity
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = 1.20 * quantity
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = 0.85 * quantity
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45 * quantity
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = 2.70 * quantity
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = 5.50 * quantity
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = 3.85 * quantity
        print(f'{price:.2f}')


if day_from_week in ('Sunday', 'Saturday'):
    if fruit == 'banana':
        price = 2.70 * quantity
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = 1.25 * quantity
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = 0.90 * quantity
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60 * quantity
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = 3.00 * quantity
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = 5.60 * quantity
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = 4.20 * quantity
        print(f'{price:.2f}')

if price == 0:
    print('error')



