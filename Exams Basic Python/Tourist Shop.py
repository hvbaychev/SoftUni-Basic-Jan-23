money = float(input())
start_money = money
count_purch = 0
product_count_sales = 0
total_sum = 0
command_stop = False
while True:
    command = input()
    if command == 'Stop':
        command_stop = True
        break
    product_count_sales += 1
    count_purch += 1
    price_product = float(input())
    if product_count_sales == 3:
        price_product *= 0.50
        product_count_sales = 0

    money -= price_product

    if money < 0:
        break

    total_sum += price_product


if command_stop:
    print(f"You bought {count_purch} products for {total_sum:.2f} leva.")
else:
    diff = abs(money)
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")


