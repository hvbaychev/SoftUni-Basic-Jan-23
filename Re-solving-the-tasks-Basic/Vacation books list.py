pages_book = int(input())
read_one_hour = int(input())
day_for_book = int(input())

total_time = pages_book / read_one_hour
time_per_day = total_time / day_for_book

print(f'{time_per_day:.0f}')