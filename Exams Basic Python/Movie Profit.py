movie_name = input()
days = int(input())
ticket_number = int(input())
ticket_price = float(input())
cinema_tax = int(input())


day_ticket_price = ticket_number * ticket_price
period_ticket_price = days * day_ticket_price

tax = period_ticket_price * (cinema_tax / 100)

total_sum = period_ticket_price - tax

print(f"The profit from the movie {movie_name} is {total_sum:.2f} lv.")