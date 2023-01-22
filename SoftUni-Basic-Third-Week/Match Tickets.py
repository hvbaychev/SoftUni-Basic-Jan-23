money = float(input())
category = input()
people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99

ticket_price = 0
transport = 0

if 1 <= people <= 4:
    transport = money * 0.75
elif 5 <= people <= 9:
    transport = money * 0.60
elif 10 <= people <= 24:
    transport = money * 0.50
elif 25 <= people <= 49:
    transport = money * 0.40
else:
    transport = money * 0.25

remain_money = money - transport

if category == 'VIP':
    ticket_price = vip_ticket * people
elif category == 'Normal':
    ticket_price = normal_ticket * people

if ticket_price > remain_money:
    remain_money = abs(ticket_price - remain_money)
    print(f'Not enough money! You need {remain_money:.2f} leva.')
else:
    remain_money = abs(remain_money - ticket_price)
    print(f'Yes! You have {remain_money:.2f} leva left.')