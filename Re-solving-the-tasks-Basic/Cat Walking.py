min_per_day = int(input())
per_day = int(input())
calories = int(input())


walk = min_per_day * per_day
total_calories = walk * 5

calories = calories * 0.50

if total_calories >= calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.')
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")