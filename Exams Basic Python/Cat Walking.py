walk_min = float(input())
walk_count = float(input())
calories = float(input())


total_walk = walk_min * walk_count
total_burn_calories = total_walk * 5
calories_half = calories * 0.50

if total_burn_calories >= calories_half:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_burn_calories:.0f}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_burn_calories:.0f}.')