import math

height = int(input())
width = int(input())
total_area_uncover = int(input())

total_paint = 0
area = (height * width * 4) * (total_area_uncover/100)
total_area = (height * width * 4) - area

while total_paint <= total_area:
    paint_litter = input()
    if paint_litter == 'Tired!':
        diff = math.ceil(abs(total_area - total_paint))
        print(f"{diff:.0f} quadratic m left.")
        break
    paint_litter = int(paint_litter)

    total_paint += paint_litter

    if total_paint > total_area:
        diff = math.ceil(abs(total_area - total_paint))
        print(f'All walls are painted and you have {diff:.0f} l paint left!')
        break
    elif total_area == total_paint:
        print("All walls are painted! Great job, Pesho!")
        break



