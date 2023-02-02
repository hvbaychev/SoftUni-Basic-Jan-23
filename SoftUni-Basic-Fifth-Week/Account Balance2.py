balance = 0
line = input()

while line != "NoMoreMoney":
    current_amount = float(line)

    if current_amount < 0:
        print("Invalid operation!")
        break

    balance += current_amount
    print(f'Increase: {current_amount:.2f}')

    line = input()

print(f'Total: {balance:.2f}')