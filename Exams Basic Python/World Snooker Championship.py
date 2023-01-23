stage_of_championship = input()
ticket = input()
ticket_count = int(input())
photo = input()

price = 0
ticket_price = 0

if ticket == 'Standard':
    if stage_of_championship == 'Quarter final':
        price = 55.50
    elif stage_of_championship == 'Semi final':
        price = 75.88
    elif stage_of_championship == 'Final':
        price = 110.10

if ticket == 'Premium':
    if stage_of_championship == 'Quarter final':
        price = 105.20
    elif stage_of_championship == 'Semi final':
        price = 125.22
    elif stage_of_championship == 'Final':
        price = 160.66

if ticket == 'VIP':
    if stage_of_championship == 'Quarter final':
        price = 118.90
    elif stage_of_championship == 'Semi final':
        price = 300.40
    elif stage_of_championship == 'Final':
        price = 400


ticket_price = price * ticket_count

if ticket_price > 4000:
    ticket_price = ticket_price * 0.75
    ticket_price = ticket_price - (40 * ticket_count)
elif ticket_price > 2500:
    ticket_price = ticket_price * 0.90

if photo == 'Y':
    ticket_price = ticket_price + (40 * ticket_count)
else:
    ticket_price = ticket_price


print(f'{ticket_price:.2f}')