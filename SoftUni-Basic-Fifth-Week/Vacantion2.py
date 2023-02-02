excursion_money = float(input())
money_hand = float(input())

count_spend = 0
save_spend = 0
total_sum = money_hand
days = 0

spend = 'True'

while total_sum < excursion_money:
    moves = input()
    money = float(input())
    days += 1
    if moves == 'spend':
        count_spend += 1
        total_sum = total_sum - money
        if money_hand < money:
            total_sum = 0
    elif moves == 'save':
        total_sum = total_sum + money
        count_spend = 0

    if count_spend == 5:
        spend = 'False'
        break

if spend == 'False':
    print("You can't save the money.")
    print(f'{days}')
elif total_sum >= excursion_money:
    print(f'You saved the money for {days} days.')


