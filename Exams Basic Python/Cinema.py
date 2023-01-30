capacity = int(input())

ticket_price = 5
sum_ticket_price = 0
sum_entrance_people = 0
entrance_people = ''

while True:
    entrance_people = input()
    if entrance_people == 'Movie time!':
        diff = abs(capacity - sum_entrance_people)
        print(f"There are {diff} seats left in the cinema.")
        print(f"Cinema income - {sum_ticket_price} lv.")
        break
    ent_int_people = int(entrance_people)

    sum_entrance_people += ent_int_people
    sum_ticket_price += ent_int_people * ticket_price

    if ent_int_people % 3 == 0:
        sum_ticket_price = sum_ticket_price - 5

    if sum_entrance_people + ent_int_people > capacity:
        print("The cinema is full.")
        print(f"Cinema income - {sum_ticket_price} lv.")
        break

    if sum_entrance_people == capacity:
        diff = abs(sum_entrance_people - capacity)
        print(f"There are {diff} seats left in the cinema.")
        print(f"Cinema income - {sum_ticket_price} lv.")
        break
