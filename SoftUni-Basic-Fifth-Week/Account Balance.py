total_sum = 0

command = 'NoMoreMoney'

while True:
    money = input()
    if money == 'NoMoreMoney':
        break

    money = float(money)
    if money <= 0:
        print('Invalid operation!')
        break
    total_sum += money

    print(f'Increase: {money:.2f}')

print(f'Total: {total_sum}')