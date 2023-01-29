revenue = float(input())
price_drink = 0
len_of_the_drink = 0
total_sum = 0

while total_sum <= revenue:
    name_of_drink = input()
    if name_of_drink == 'Party!':
        diff = abs(revenue - total_sum)
        print(f"We need {diff:.2f} leva more.")
        print(f"Club income - {total_sum:.2f} leva.")
        break

    number_drink = int(input())

    len_of_the_drink = len(name_of_drink)
    price_drink = len_of_the_drink * number_drink

    if price_drink % 2 == 1:
        price_drink = price_drink * 0.75

    total_sum += price_drink

    if total_sum >= revenue:
        print("Target acquired.")
        print(f"Club income - {total_sum:.2f} leva.")
        break



