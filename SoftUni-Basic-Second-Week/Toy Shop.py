price_excursion = float(input())

puzzel_order = int(input())
doll_order = int(input())
teddy_order = int(input())
minion_order = int(input())
truck_order = int(input())

puzzel_price = puzzel_order * 2.60
talking_doll_price = doll_order * 3.00
teddy_bear_price = teddy_order * 4.10
minion_price = minion_order * 8.20
truck_price = truck_order * 2.00

total_order_toys = puzzel_order + doll_order + teddy_order + minion_order + truck_order
total_price = puzzel_price + talking_doll_price + teddy_bear_price + minion_price + truck_price

if total_order_toys >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.90
diff = abs(price_excursion - total_price)

if price_excursion <= total_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
