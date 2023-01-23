guest = int(input())
reserve = float(input())
money = float(input())

total_sum = 0
cake = 0



if guest >= 10 and guest <= 15:
    total_sum = (guest * reserve) * 0.85
elif guest > 15 and guest <= 20:
    total_sum = (guest * reserve) * 0.80
elif guest > 20:
    total_sum = (guest * reserve) * 0.75
else:
    total_sum = guest * reserve

cake_price = money * 0.10

total_sum = total_sum + cake_price
remain_money = abs(money - total_sum)

if money > total_sum:
    print(f'It is party time! {remain_money:.2f} leva left.')
else:
    print(f"No party! {remain_money:.2f} leva needed.")