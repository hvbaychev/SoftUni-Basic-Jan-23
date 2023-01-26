period = int(input())
water = 20
internet = 15
other_expenses = 0
average = 0

total_electricity = 0
total_water = 20 * period
total_internet = 15 * period


for month in range(period):
    electricity = float(input())
    total_electricity += electricity
    other_expenses += (electricity + water + internet) * 1.20


average = (total_electricity + total_water + total_internet + other_expenses) / period

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {other_expenses:.2f} lv')
print(f'Average: {average:.2f} lv')