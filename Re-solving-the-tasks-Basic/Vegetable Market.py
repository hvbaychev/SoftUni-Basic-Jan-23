price_veg = float(input())
price_fruit = float(input())
kg_total_veg = float(input())
kg_total_fruit = float(input())

price_veg = price_veg * kg_total_veg
price_fruit = price_fruit * kg_total_fruit

total = (price_fruit + price_veg) / 1.94

print(f'{total:.2f}')
