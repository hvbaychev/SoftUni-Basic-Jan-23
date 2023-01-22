type_of_flowers = input()
amount_flowers = int(input())
money = float(input())

final_price = 0.00
sum_flowers = 0.00

rose = 5
dalia = 3.80
lale = 2.80
narcis = 3.00
gladiola = 2.50

if type_of_flowers == 'Roses':
    sum_flowers = rose * amount_flowers
    final_price = abs(money - sum_flowers)
    if amount_flowers > 80:
        sum_flowers = rose * 0.9 * amount_flowers
        final_price = abs(money - sum_flowers)
        print(final_price)


if type_of_flowers == 'Dahlias':
    sum_flowers = dalia * amount_flowers
    final_price = abs(money - sum_flowers)
    if amount_flowers > 90:
        sum_flowers = dalia * 0.85 * amount_flowers
        final_price = abs(money - sum_flowers)


if type_of_flowers == 'Tulips':
    sum_flowers = lale * amount_flowers
    final_price = abs(money - sum_flowers)
    if amount_flowers > 80:
        sum_flowers = lale * 0.85 * amount_flowers
        final_price = abs(money - sum_flowers)

if type_of_flowers == 'Narcissus':
    if amount_flowers < 120:
        price_narcis = narcis * amount_flowers
        price_after_incr = price_narcis * 0.15
        sum_flowers = price_narcis + price_after_incr
        final_price = abs(sum_flowers- money)
    elif amount_flowers >= 120:
        sum_flowers = narcis * amount_flowers
        final_price = abs(sum_flowers - money)

if type_of_flowers == 'Gladiolus':
    if amount_flowers < 80:
        price_glad = gladiola * amount_flowers
        price_after_incr = price_glad * 0.20
        sum_flowers = price_after_incr + price_glad
        final_price = abs(sum_flowers - money)
    elif amount_flowers >= 80:
        sum_flowers = gladiola * amount_flowers
        final_price = abs(sum_flowers - money)

if money < sum_flowers:
    print(f'Not enough money, you need {final_price:.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {amount_flowers} {type_of_flowers} and {final_price:.2f} leva left.')
