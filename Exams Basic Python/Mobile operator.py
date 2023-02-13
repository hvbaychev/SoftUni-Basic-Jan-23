contract = input()
name_contract = input()
extra_data = input()
month_for_pay = int(input())
total_sum = 0
price = 0

if contract == 'one':
    if name_contract == 'Small':
        price = 9.98
    elif name_contract == 'Middle':
        price = 18.99
    elif name_contract == 'Large':
        price = 25.98
    elif name_contract == 'ExtraLarge':
        price = 35.99
elif contract == 'two':
    if name_contract == 'Small':
        price = 8.58
    elif name_contract == 'Middle':
        price = 17.09
    elif name_contract == 'Large':
        price = 23.59
    elif name_contract == 'ExtraLarge':
        price = 31.79

if price <= 10.00:
    if extra_data == 'yes':
        price += 5.50
elif 10.00 < price <= 30.00:
    if extra_data == 'yes':
        price += 4.35
elif price > 30.00:
    if extra_data == 'yes':
        price += 3.85

if contract == 'two':
    price = price * 0.9625

total_sum = price * month_for_pay

print(f'{total_sum:.2f} lv.')