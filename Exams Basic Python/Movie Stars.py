budjet = float(input())

money_income = 0
total_money_income = 0
len_of_the_name = 0
salary = 0
remain_budjet = budjet

money_for_actor = 'false'

while True:
    name_actor = input()
    if name_actor == 'ACTION':
        if budjet > remain_budjet:
            break
    len_of_the_name = len(name_actor)
    if len_of_the_name > 15:
        money_income = remain_budjet * 0.20
    else:
        salary = float(input())
        money_income = salary

    total_money_income += money_income
    remain_budjet = budjet - total_money_income

    if budjet < total_money_income:
        money_for_actor = 'true'
        break


if money_for_actor == 'true':
    print(f"We need {abs(total_money_income - budjet):.2f} leva for our actors.")
else:
    print(f"We are left with {abs(budjet - total_money_income):.2f} leva.")