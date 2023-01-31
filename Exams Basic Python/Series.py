money = float(input())
number_series = int(input())

total_sum = 0

for _ in range(number_series):
    name_of_serial = input()
    price_of_serial = float(input())

    if name_of_serial == 'Thrones':
        tax = price_of_serial * 0.50
    elif name_of_serial == 'Lucifer':
        tax = price_of_serial * 0.60
    elif name_of_serial == 'Protector':
        tax = price_of_serial * 0.70
    elif name_of_serial == 'TotalDrama':
        tax = price_of_serial * 0.80
    elif name_of_serial == 'Area':
        tax = price_of_serial * 0.90
    else:
        tax = price_of_serial

    total_sum += tax

diff = abs(money - total_sum)
if money >= total_sum:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")