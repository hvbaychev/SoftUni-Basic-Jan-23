import math

number_people = int(input())
enter_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

enter_total_tax = number_people * enter_tax

sunbed_needed = math.ceil(number_people * 0.75)
sunbed_total_price = (sunbed_needed * sunbed_price)

umbrella_needed = math.ceil(number_people * 0.50)
umbrella_total_price = umbrella_needed * umbrella_price

final_sum = enter_total_tax + sunbed_total_price + umbrella_total_price

print(f'{final_sum:.2f} lv.')