import math

count_magnolias = int(input())
count_hyacinths = int(input())
count_rose = int(input())
count_cactus = int(input())
price_gift = float(input())


price_magnolias = 3.25 * count_magnolias
price_hyacinths = 4 * count_hyacinths
price_rose = 3.50 * count_rose
price_cactus = 8 * count_cactus

total_sum_flowers = price_magnolias + price_hyacinths + price_rose + price_cactus

total_sum_tax = total_sum_flowers * 0.05
total_sum_flowers = total_sum_flowers - total_sum_tax

if price_gift > total_sum_flowers:
    diff = abs(price_gift - total_sum_flowers)
    diff = math.ceil(diff)
    print(f'She will have to borrow {diff:.0f} leva.')
else:
    diff = abs(total_sum_flowers - price_gift)
    diff = math.floor(diff)
    print(f'She is left with {diff:.0f} leva.')


