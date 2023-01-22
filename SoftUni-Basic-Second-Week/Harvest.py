from math import floor, ceil

square_meter_grapes_field = int(input())
grapes_per_square_meter = float(input())
need_wine = int(input())
number_of_workers = int(input())

save_qrapes = 0.40
one_litter = 2.5

total_grapes = square_meter_grapes_field * grapes_per_square_meter
total_wine = (save_qrapes * total_grapes) / one_litter

if total_wine >= need_wine:
    wine_per_person = abs(total_wine - need_wine)
    liter_per_person = abs(wine_per_person / number_of_workers)
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.'
          f'\n{ceil(wine_per_person)} liters left -> {ceil(liter_per_person)} liters per person.')
else:
    more_wine_need = abs(need_wine - total_wine)
    print(f"It will be a tough winter! More {floor(more_wine_need)} liters wine needed.")
