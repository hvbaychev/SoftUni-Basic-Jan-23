flower = input()
qty = int(input())
budget = int(input())

flower_price = 0
if flower == "Roses":
    flower_price = 5 * 0.9 if qty > 80 else 5
elif flower == "Dahlias":
    flower_price = 3.8 * 0.85 if qty > 90 else 3.8
elif flower == "Tulips":
    flower_price = 2.8 * 0.85 if qty > 80 else 2.8
elif flower == "Narcissus":
    flower_price = 3 * 1.15 if qty < 120 else 3
elif flower == "Gladiolus":
    flower_price = 2.5 * 1.2 if qty < 80 else 2.5

total_price = qty * flower_price
result = abs(total_price - budget)

if total_price > budget:
    print(f"Not enough money, you need {result:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {qty} {flower} and {result:.2f} leva left.")