budjet = float(input())
number_nights = int(input())
night_price = float(input())
more_expenses = int(input())


if number_nights > 7:
    night_price = night_price * 0.95

total_exp_night = number_nights * night_price

more_expenses = (more_expenses / 100) * budjet

total_sum = total_exp_night + more_expenses

diff = abs(budjet - total_sum)
if total_sum <= budjet:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")