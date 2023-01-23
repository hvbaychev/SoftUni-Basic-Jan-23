price_baggage_20 = float(input())
baggage_kg = float(input())
days_to_travel = int(input())
number_baggage = int(input())


total_sum = 0

if baggage_kg < 10:
    total_sum = price_baggage_20 * 0.20
elif 10 <= baggage_kg <= 20:
    total_sum = price_baggage_20 * 0.50
else:
    total_sum = price_baggage_20

if days_to_travel > 30:
    total_sum += total_sum * 0.10
elif 30 >= days_to_travel >= 7:
    total_sum += total_sum * 0.15
elif days_to_travel < 7:
    total_sum += total_sum * 0.40

total_sum = total_sum * number_baggage

print(f'The total price of bags is: {total_sum:.2f} lv.')
