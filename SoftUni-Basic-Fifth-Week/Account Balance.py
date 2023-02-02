total_sum = 0

command = 'NoMoreMoney'
money_text = 'true'
money_less = 'true'

while True:
    money = input()
    if money == 'NoMoreMoney':
        money_text = 'false'
        break

    money = float(money)
    if money < 0:
        money_less = 'false'
        print('Invalid operation!')
        break

    total_sum += money
    print(f'Increase: {money:.2f}')

if money_text == 'false' or money_less == 'false':
    print(f'Total: {total_sum}')
