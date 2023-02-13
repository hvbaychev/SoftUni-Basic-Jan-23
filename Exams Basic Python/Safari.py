money = float(input())
gasoline_liters = float(input())
day_of_week = input()

gasoline = 2.10
gide = 100
saturday = 0.10
sunday = 0.20

gasoline_price = gasoline * gasoline_liters
total_price = gasoline_price + gide

if day_of_week == 'Saturday':
    total_price = total_price * 0.90
elif day_of_week == 'Sunday':
    total_price = total_price * 0.80


diff = abs(money - total_price)
if money > total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")