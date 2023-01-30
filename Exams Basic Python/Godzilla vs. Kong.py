budjet = float(input())
extras = int(input())
clothes_price = float(input())


decor = budjet * 0.10
sum_for_clothes = clothes_price * extras

if extras > 150:
    sum_for_clothes = sum_for_clothes * 0.90

total_sum = decor + sum_for_clothes

diff = abs(total_sum - budjet)

if total_sum <= budjet:
    print("Action!")
    print(f"Wingard starts filming with {diff:.02f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")