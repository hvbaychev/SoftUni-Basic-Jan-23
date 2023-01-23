import math

tennis_rocket = float(input())
count_rocket = int(input())
snickers = int(input())

rocket_price = count_rocket * tennis_rocket
snickers_price = tennis_rocket / 6
snickers_price = snickers_price * snickers

rest_equip_price = (rocket_price + snickers_price) * 0.20

total_sum = rocket_price + snickers_price + rest_equip_price

price_djok = math.floor(total_sum / 8)
price_rest = math.ceil(total_sum * 7/8)

print(f"Price to be paid by Djokovic {price_djok:.0f}")
print(f"Price to be paid by sponsors {price_rest}")

