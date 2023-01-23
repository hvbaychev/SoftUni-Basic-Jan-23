import sys

number_of_pvc = int(input())
type_of_pvc = str(input())
delivery = str(input())

delivery_sum = 60
price = 0

if number_of_pvc < 10:
    print("Invalid order")
    sys.exit()

if type_of_pvc == "90X130":
    if 30 < number_of_pvc <= 60:
        price = (number_of_pvc * 110) * 0.95
    elif number_of_pvc > 60:
        price = (number_of_pvc * 110) * 0.92
    else:
        price = (number_of_pvc * 110)
if type_of_pvc == "100X150":
    if 40 < number_of_pvc <= 80:
        price = (number_of_pvc * 140) * 0.94
    elif number_of_pvc > 80:
        price = (number_of_pvc * 140) * 0.90
    else:
        price = (number_of_pvc * 140)
if type_of_pvc == "130X180":
    if 20 < number_of_pvc <= 50:
        price = (number_of_pvc * 190) * 0.93
    elif number_of_pvc > 50:
        price = (number_of_pvc * 190) * 0.86
    else:
        price = (number_of_pvc * 190)
if type_of_pvc == "200X300":
    if 20 < number_of_pvc <= 50:
        price = (number_of_pvc * 250) * 0.91
    elif number_of_pvc > 50:
        price = (number_of_pvc * 250) * 0.86
    else:
        price = (number_of_pvc * 250)

if delivery == "With delivery":
    final_sum = delivery_sum + price
else:
    delivery == "Without delivery"
    final_sum = price
if number_of_pvc >= 99:
    final_sum = (final_sum - (final_sum * 0.04))
else:
    final_sum = final_sum
print(f"{final_sum:.2f} BGN")
