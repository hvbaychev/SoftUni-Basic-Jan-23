import math

holidays = int(input())
food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_kg = float(input())

dog_food_per_day = holidays * food_for_dog_kg
cat_food_per_day = holidays * food_for_cat_kg
turtle_food_per_day = (holidays * food_for_turtle_kg) / 1000

total_food_animal = dog_food_per_day + cat_food_per_day + turtle_food_per_day

if food_kg >= total_food_animal:
    remain_food = food_kg - total_food_animal
    remain_food = math.floor(remain_food)
    print(f'{remain_food:.0f} kilos of food left.')
else:
    remain_food = abs(food_kg - total_food_animal)
    remain_food = math.ceil(remain_food)
    print(f'{remain_food:.0f} more kilos of food are needed.')
