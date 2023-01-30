movie_name = input()
packet = input()
ticket_number = int(input())

price = 0
total_sum = 0

if movie_name == 'John Wick':
    if packet == 'Drink':
        price = 12
    elif packet == 'Popcorn':
        price = 15
    elif packet == 'Menu':
        price = 19

if movie_name == 'Star Wars':
    if packet == 'Drink':
        price = 18
    elif packet == 'Popcorn':
        price = 25
    elif packet == 'Menu':
        price = 30

if movie_name == 'Jumanji':
    if packet == 'Drink':
        price = 9
    elif packet == 'Popcorn':
        price = 11
    elif packet == 'Menu':
        price = 14

total_sum += price * ticket_number

if movie_name == 'Star Wars' and ticket_number >= 4:
    total_sum = total_sum * 0.70
elif movie_name == 'Jumanji' and ticket_number == 2:
    total_sum = total_sum * 0.85

print(f"Your bill is {total_sum:.2f} leva.")
