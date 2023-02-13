strawberries_price = float(input())

bananas_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())


raspberries_price = strawberries_price * 0.50
orange_price = raspberries_price * 0.60
banana_price = raspberries_price * 0.20

raspberries_price = raspberries_price * raspberries_kg
orange_price = orange_price * orange_kg
banana_price = banana_price * bananas_kg
strawberries_price = strawberries_price * strawberries_kg

total_sum = raspberries_price + orange_price + banana_price + strawberries_price

print(f'{total_sum:.2f}')