name_air = input()
ticket_adult_count = int(input())
ticket_child_count = int(input())
ticket_adult_price = float(input())
taxes = float(input())

net_ticket_child = ticket_adult_price * 0.30

net_ticket_child = net_ticket_child + taxes
ticket_adult_price = ticket_adult_price + taxes

total_sum = (ticket_adult_count * ticket_adult_price) + (ticket_child_count * net_ticket_child)

total_win_money = total_sum * 0.20

print(f'The profit of your agency from {name_air} tickets is {total_win_money:.2f} lv.' )