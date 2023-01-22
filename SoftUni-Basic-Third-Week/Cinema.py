screening_type = input()
column = int(input())
row = int(input())

premiere = 12.00
normal = 7.50
discount_ticket = 5.00

revenue = 0.00

capacity_cinema = column * row

if screening_type == 'Premiere':
    revenue = capacity_cinema * premiere
elif screening_type == 'Normal':
    revenue = capacity_cinema * normal
elif screening_type == 'Discount':
    revenue = capacity_cinema * discount_ticket

print(f'{revenue:.2f} leva')