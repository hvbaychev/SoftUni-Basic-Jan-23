food_for_dog = int(input())
is_adopted = False
food_in_gram = food_for_dog * 1000
total_food = 0

while True:
    eat_from_dog = input()
    if eat_from_dog == 'Adopted':
        is_adopted = True
        break

    quantity = int(eat_from_dog)
    total_food += quantity

diff = abs(food_in_gram - total_food)
if food_in_gram >= total_food:
    print(f"Food is enough! Leftovers: {diff:.0f} grams.")
else:
    print(f"Food is not enough. You need {diff:.0f} grams more.")