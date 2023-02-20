target = int(input())

men_price = 15
ladies_price = 20
kids_price = 10

touch_up_price = 20
full_color_price = 30

total_income = 0

while True:
    type_service = input()
    if type_service == 'closed':
        break

    if type_service == 'haircut':
        service = input()
        if service == 'mens':
            total_income = total_income + men_price
        elif service == 'ladies':
            total_income = total_income + ladies_price
        elif service == 'kids':
            total_income = total_income + kids_price

    if type_service == 'color':
        service = input()
        if service == 'touch up':
            total_income = total_income + touch_up_price
        elif service == 'full color':
            total_income = total_income + full_color_price

    if target <= total_income:
        break

if target <= total_income:
    print("You have reached your target for the day!")
    print(f"Earned money: {total_income:.0f}lv.")
elif target > total_income:
    diff = abs(total_income - target)
    print(f"Target not reached! You need {diff:.0f}lv. more.")
    print(f"Earned money: {total_income:.0f}lv.")
