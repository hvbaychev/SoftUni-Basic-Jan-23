easter_bread = int(input())
eggs = int(input())
cookies_kg = int(input())


easter_bread_price = 3.20 * easter_bread
eggs_price = 4.35 * eggs
cookies_price = 5.40 * cookies_kg
paint_for_eggs = 0.15
eggs_in_carton = 12

paint_for_all_eggs = eggs * eggs_in_carton * paint_for_eggs

total_sum = easter_bread_price + eggs_price + cookies_price + paint_for_all_eggs

print(f'{total_sum:0.2f}')