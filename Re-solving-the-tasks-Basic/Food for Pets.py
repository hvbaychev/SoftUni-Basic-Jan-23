days = int(input())
total_food = float(input())

cat_food = 0
dog_food = 0
biscuit = 0
total_eat_food = 0


for i in range(1, days+1):
    eat_for_dog_per_day = int(input())
    eat_for_cat_per_day = int(input())
    if i % 3 == 0:
        cat_food += eat_for_cat_per_day
        dog_food += eat_for_dog_per_day
        biscuit += (eat_for_dog_per_day + eat_for_cat_per_day) * 0.10
    else:
        cat_food += eat_for_cat_per_day
        dog_food += eat_for_dog_per_day


total_eat_food = cat_food + dog_food
percent_total_eat = (total_eat_food / total_food) * 100
percent_total_eat_dog = (dog_food / total_eat_food) * 100
percent_total_eat_cat = (cat_food / total_eat_food) * 100


print(f'Total eaten biscuits: {biscuit:.0f}gr.')
print(f'{percent_total_eat:.2f}% of the food has been eaten.')
print(f'{percent_total_eat_dog:.2f}% eaten from the dog.')
print(f'{percent_total_eat_cat:.2f}% eaten from the cat.')

