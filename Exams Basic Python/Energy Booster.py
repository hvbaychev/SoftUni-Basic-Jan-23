fruit = input()
size_set = input()
quantity = int(input())

watermelon_price = 0
mango_price = 0
pineapple_price = 0
raspberry_price = 0

size_of_pack_small = 2
size_of_pack_big = 5

total_sum = 0

if size_set == 'small':
    watermelon_price = 56 * size_of_pack_small
    mango_price = 36.66 * size_of_pack_small
    pineapple_price = 42.10 * size_of_pack_small
    raspberry_price = 20 * size_of_pack_small
elif size_set == 'big':
    watermelon_price = 28.70 * size_of_pack_big
    mango_price = 19.60 * size_of_pack_big
    pineapple_price = 24.80 * size_of_pack_big
    raspberry_price = 15.20 * size_of_pack_big

if fruit == 'Watermelon':
    total_sum = watermelon_price * quantity
elif fruit == 'Mango':
    total_sum = mango_price * quantity
elif fruit == 'Pineapple':
    total_sum = pineapple_price * quantity
elif fruit == 'Raspberry':
    total_sum = raspberry_price * quantity

if 400 <= total_sum <= 1000:
    total_sum = total_sum * 0.85
elif total_sum > 1000:
    total_sum = total_sum * 0.50

print(f'{total_sum:.2f} lv.')