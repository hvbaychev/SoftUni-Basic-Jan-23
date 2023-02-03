money_need = int(input())

total_sum_donate = 0

count = 0
cash_pay = 0
card_pay = 0

sum_cash = 0
sum_card = 0
average_cash = 0
average_card = 0

change_name = 'False'
change_value = 'False'

while True:
    command = input()
    if command == 'End':
        change_name = 'True'
        break

    count += 1
    charity_money = int(command)

    if count % 2 == 0:
        if charity_money < 10:
            print('Error in transaction!')
        elif charity_money >= 10:
            total_sum_donate += charity_money
            card_pay += 1
            sum_card += charity_money
            average_card = sum_card / card_pay
            print('Product sold!')
    else:
        if charity_money > 100:
            print('Error in transaction!')
        elif charity_money <= 100:
            total_sum_donate += charity_money
            cash_pay += 1
            sum_cash += charity_money
            average_cash = sum_cash / cash_pay
            print('Product sold!')

    if money_need <= total_sum_donate:
        change_value = 'True'
        break

if change_name == 'True':
    print('Failed to collect required money for charity.')
elif change_value == 'True':
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')