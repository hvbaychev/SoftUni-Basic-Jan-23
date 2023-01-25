age = int(input())
laundry_price = float(input())
toy_price = float(input())

bthday_money = 0
current_sum = 10
brother_tax = 0
count = 0
toy_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        count += 1
        brother_tax += 1
        bthday_money = bthday_money + current_sum * count
    else:
        toy_count += 1

total_save_money = bthday_money + (toy_price * toy_count) - brother_tax
diff = abs(total_save_money - laundry_price)
if total_save_money >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
