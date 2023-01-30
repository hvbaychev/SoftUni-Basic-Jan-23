movies_name = input()
hall_type = input()
ticket_sales = int(input())

total_sum = 0
ticket_price = 0

if movies_name == 'A Star Is Born':
    if hall_type == 'normal':
        ticket_price = 7.50
        total_sum = total_sum + ticket_price
    elif hall_type == 'luxury':
        ticket_price = 10.50
        total_sum = total_sum + ticket_price
    elif hall_type == 'ultra luxury':
        ticket_price = 13.50
        total_sum = total_sum + ticket_price

if movies_name == 'Bohemian Rhapsody':
    if hall_type == 'normal':
        ticket_price = 7.35
        total_sum = total_sum + ticket_price
    elif hall_type == 'luxury':
        ticket_price = 9.45
        total_sum = total_sum + ticket_price
    elif hall_type == 'ultra luxury':
        ticket_price = 12.75
        total_sum = total_sum + ticket_price

if movies_name == 'Green Book':
    if hall_type == 'normal':
        ticket_price = 8.15
        total_sum = total_sum + ticket_price
    elif hall_type == 'luxury':
        ticket_price = 10.25
        total_sum = total_sum + ticket_price
    elif hall_type == 'ultra luxury':
        ticket_price = 13.25
        total_sum = total_sum + ticket_price

if movies_name == 'The Favourite':
    if hall_type == 'normal':
        ticket_price = 8.75
        total_sum = total_sum + ticket_price
    elif hall_type == 'luxury':
        ticket_price = 11.55
        total_sum = total_sum + ticket_price
    elif hall_type == 'ultra luxury':
        ticket_price = 13.95
        total_sum = total_sum + ticket_price


total_sum = total_sum * ticket_sales

print(f"{movies_name} -> {total_sum:.2f} lv.")

