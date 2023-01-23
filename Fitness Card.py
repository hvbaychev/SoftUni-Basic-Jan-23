money = float(input())
gender = input()
age = int(input())
sport = input()


total_sum = 0

if gender == 'm':
    gym_price = 42
    boxing_price = 41
    yoga_price = 45
    zumba_price = 34
    dances_price = 51
    pilates_price = 39
elif gender == 'f':
    gym_price = 35
    boxing_price = 37
    yoga_price = 42
    zumba_price = 31
    dances_price = 53
    pilates_price = 37

if sport == 'Gym' and gender == 'm':
    total_sum = gym_price
elif sport == 'Boxing' and gender == 'm':
    total_sum = boxing_price
elif sport == 'Yoga' and gender == 'm':
    total_sum = yoga_price
elif sport == 'Zumba' and gender == 'm':
    total_sum = zumba_price
elif sport == 'Dances' and gender == 'm':
    total_sum = dances_price
elif sport == 'Pilates' and gender == 'm':
    total_sum = pilates_price


if sport == 'Gym' and gender == 'f':
    total_sum = gym_price
elif sport == 'Boxing' and gender == 'f':
    total_sum = boxing_price
elif sport == 'Yoga' and gender == 'f':
    total_sum = yoga_price
elif sport == 'Zumba' and gender == 'f':
    total_sum = zumba_price
elif sport == 'Dances' and gender == 'f':
    total_sum = dances_price
elif sport == 'Pilates' and gender == 'f':
    total_sum = pilates_price


if age <= 19:
    total_sum = total_sum * 0.80

if total_sum <= money:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    total_sum = abs(total_sum - money)
    print(f"You don't have enough money! You need ${total_sum:.2f} more.")
