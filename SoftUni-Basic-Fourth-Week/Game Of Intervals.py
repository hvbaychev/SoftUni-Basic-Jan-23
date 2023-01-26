roll_game = int(input())

result_of_game = 0

count_invalid_number = 0
count_zero_nine = 0
count_ten_ninghteen = 0
count_twenty_twentynine = 0
count_thirty_thirthynine = 0
count_fourthy_fifthy = 0

for game in range(roll_game):
    new_number = float(input())
    if new_number < 0 or new_number > 50:
        result_of_game = result_of_game / 2
        count_invalid_number += 1
    elif 0 <= new_number <= 9:
        result_of_game += new_number * 0.20
        count_zero_nine += 1
    elif 10 <= new_number <= 19:
        result_of_game += new_number * 0.30
        count_ten_ninghteen += 1
    elif 20 <= new_number <= 29:
        result_of_game += new_number * 0.40
        count_twenty_twentynine += 1
    elif 30 <= new_number <= 39:
        result_of_game += 50
        count_thirty_thirthynine += 1
    elif 40 <= new_number <= 50:
        result_of_game += 100
        count_fourthy_fifthy += 1

p1 = (count_zero_nine / roll_game) * 100
p2 = (count_ten_ninghteen / roll_game) * 100
p3 = (count_twenty_twentynine / roll_game) * 100
p4 = (count_thirty_thirthynine / roll_game) * 100
p5 = (count_fourthy_fifthy / roll_game) * 100
p6 = (count_invalid_number / roll_game) * 100


print(f'{result_of_game:.2f}')
print(f'From 0 to 9: {p1:.2f}%')
print(f'From 10 to 19: {p2:.2f}%')
print(f'From 20 to 29: {p3:.2f}%')
print(f'From 30 to 39: {p4:.2f}%')
print(f'From 40 to 50: {p5:.2f}%')
print(f'Invalid numbers: {p6:.2f}%')
