inherited_money = float(input())
year = int(input())

user_years = 18
spent_money_even = 0
spent_money_odd = 0
spent_per_even_year = 12000
remain_money = inherited_money

for age in range(1800, year+1):
    if age % 2 == 0:
        spent_money_even = spent_per_even_year
        remain_money = remain_money - spent_money_even
        user_years = user_years + 1
    elif age % 2 != 0:
        spent_money_odd = spent_per_even_year + (user_years * 50)
        remain_money = remain_money - spent_money_odd
        user_years = user_years + 1

if remain_money >= 0:
    print(f'Yes! He will live a carefree life and will have {remain_money:.2f} dollars left.')
else:
    diff = abs(remain_money)
    print(f'He will need {diff:.2f} dollars to survive.')

