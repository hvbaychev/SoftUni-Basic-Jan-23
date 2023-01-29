drink_type = input()
sugar = input()
drink_number = int(input())

total_sum = 0


if drink_type == 'Espresso' and sugar == 'Without':
    total_sum += 0.90
elif drink_type == 'Espresso' and sugar == 'Normal':
    total_sum += 1
elif drink_type == 'Espresso' and sugar == 'Extra':
    total_sum += 1.20


if drink_type == 'Cappuccino' and sugar == 'Without':
    total_sum += 1
elif drink_type == 'Cappuccino' and sugar == 'Normal':
    total_sum += 1.20
elif drink_type == 'Cappuccino' and sugar == 'Extra':
    total_sum += 1.60


if drink_type == 'Tea' and sugar == 'Without':
    total_sum += 0.50
elif drink_type == 'Tea' and sugar == 'Normal':
    total_sum += 0.60
elif drink_type == 'Tea' and sugar == 'Extra':
    total_sum += 0.70

total_sum = total_sum * drink_number

if sugar == 'Without':
    total_sum = total_sum * 0.65

if drink_type == 'Espresso' and drink_number >= 5:
    total_sum = total_sum * 0.75

if total_sum > 15:
    total_sum = total_sum * 0.80

print(f"You bought {drink_number} cups of {drink_type} for {total_sum:.2f} lv.")