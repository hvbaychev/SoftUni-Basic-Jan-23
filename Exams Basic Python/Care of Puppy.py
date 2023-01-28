adopted = 'Adopted'

food = int(input())
total_buy_food = food * 1000
total_eaten_food = 0


while adopted == 'Adopted':
    eaten_food_per_day = input()
    if eaten_food_per_day == adopted:
        break
    eaten_food_per_day = int(eaten_food_per_day)
    total_eaten_food += eaten_food_per_day

diff = abs(total_buy_food - total_eaten_food)

if total_buy_food >= total_eaten_food:
    print(f'Food is enough! Leftovers: {diff:.0f} grams.')
else:
    print(f"Food is not enough. You need {diff:.0f} grams more.")