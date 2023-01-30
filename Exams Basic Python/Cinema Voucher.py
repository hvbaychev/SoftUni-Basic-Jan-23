voucher = int(input())
ticket = 0
other_things = 0
total_tickets = 0
total_other = 0
price = 0
purchase = 0

while purchase != "End":
    purchase = input()
    if len(purchase) > 8:
        letter1 = purchase[0]
        letter2 = purchase[1]
        price = ord(letter1) + ord(letter2)
    elif len(purchase) <= 8:
        letter1 = purchase[0]
        price = ord(letter1)
    else:
        break

    if voucher - price >= 0:
        voucher -= price
        if len(purchase) > 8:
            ticket += 1
        elif len(purchase) <= 8 and purchase != "End":
            other_things += 1
    else:
        break

total_tickets += ticket
total_other += other_things
print(total_tickets)
print(total_other)

