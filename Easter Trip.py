destination = input()
dates = input()
nights = int(input())

total_sum = 0
price = 0

if destination == 'France':
    if dates == '21-23':
        price = 30
    elif dates == '24-27':
        price = 35
    elif dates == '28-31':
        price = 40

if destination == 'Italy':
    if dates == '21-23':
        price = 28
    elif dates == '24-27':
        price = 32
    elif dates == '28-31':
        price = 39

if destination == 'Germany':
    if dates == '21-23':
        price = 32
    elif dates == '24-27':
        price = 37
    elif dates == '28-31':
        price = 43


total_sum = price * nights

print(f"Easter trip to {destination} : {total_sum:.2f} leva.")