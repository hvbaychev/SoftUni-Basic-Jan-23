amount_pvc = int(input())
type_pvc = input()
delivery = input()

total_sum = 0
price = 0

if type_pvc == '90X130':
    price = 110 * amount_pvc
    if 30 < amount_pvc <= 60:
        total_sum = price * 0.95
    elif amount_pvc > 60:
        total_sum = price * 0.92
    else:
        total_sum = total_sum * price

if type_pvc == '100X150':
    price = 140 * amount_pvc
    if 40 < amount_pvc <= 80:
        total_sum = price * 0.94
    elif amount_pvc > 80:
        total_sum = price * 0.90
    else:
        total_sum = total_sum * price

if type_pvc == '130X180':
    price = 190 * amount_pvc
    if 20 <= amount_pvc < 50:
        total_sum = price * 0.93
    elif 50 <= amount_pvc > 99:
        total_sum = price * 0.86
    else:
        total_sum = total_sum * price

if type_pvc == '200X300':
    price = 250 * amount_pvc
    if 20 < amount_pvc < 50:
        total_sum = price * 0.91
    elif 50 <= amount_pvc > 99:
        total_sum = price * 0.86
    else:
        total_sum = total_sum * price

if delivery == 'With delivery':
    total_sum = total_sum + 60
elif delivery == 'Without delivery':
    total_sum = total_sum

if amount_pvc > 99:
    total_sum = total_sum * 0.96


if amount_pvc > 10:
    print(f'{total_sum:.2f} BGN')
else:
    print('Invalid order')

