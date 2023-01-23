tax_for_treining = int(input())

snickers_price = tax_for_treining * 0.60
equip_price = snickers_price * 0.80
ball = equip_price * 0.25
acss = ball * 0.2

total_sum = snickers_price + equip_price + ball + acss + tax_for_treining

print(f'{total_sum:.2f}')