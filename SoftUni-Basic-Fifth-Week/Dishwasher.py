number_det = int(input())

amount_det_bot = 750
dishesh = 5
pots = 15

count_times = 0

pots_number = 0
dishes_number = 0

quantity = 0
total_amount = number_det * amount_det_bot
command = input()
while True:
    if command == 'End':
        print('Detergent was enough!')
        print(f'{dishes_number} dishes and {pots_number} pots were washed.')
        print(f'Leftover detergent {total_amount} ml.')
        break

    number_plates = int(command)
    count_times += 1

    if count_times % 3 == 0:
        pots_number += number_plates
        quantity = number_plates * pots
        total_amount = total_amount - quantity
    else:
        dishes_number += number_plates
        quantity = number_plates * dishesh
        total_amount = total_amount - quantity

    if total_amount < 0:
        total_amount = abs(total_amount)
        print(f'Not enough detergent, {total_amount} ml. more necessary!')
        break

    command = input()






