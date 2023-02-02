excursion_money = float(input())
money_hand = float(input())

days = 0
count_spend = 0


while money_hand < excursion_money and count_spend < 5:
    moves = input()
    money = float(input())
    days += 1
    if moves == 'spend':
        count_spend += 1
        money_hand -= money
        if money_hand < 0:
            money_hand = 0
    elif moves == 'save':
        money_hand += money
        count_spend = 0


if count_spend == 5:
    print("You can't save the money.")
    print(f'{days}')
elif money_hand >= excursion_money:
    print(f'You saved the money for {days} days.')


