day_for_rest = int(input())
accommodation = input()
grade = input()

room = 18
apartment = 25
president_apartment = 35

day_for_rest = day_for_rest - 1

final_price = 0

if accommodation == 'room for one person':
    final_price = room * day_for_rest

if day_for_rest < 10 and accommodation == 'apartment':
    apartment = apartment * 0.70
    final_price = apartment * day_for_rest
elif 10 <= day_for_rest <= 15 and accommodation == 'apartment':
    apartment = apartment * 0.65
    final_price = apartment * day_for_rest
elif day_for_rest > 15 and accommodation == 'apartment':
    apartment = apartment * 0.50
    final_price = apartment * day_for_rest

if day_for_rest < 10 and accommodation == 'president apartment':
    president_apartment = president_apartment * 0.90
    final_price = president_apartment * day_for_rest
elif 10 <= day_for_rest <= 15 and accommodation == 'president apartment':
    president_apartment = president_apartment * 0.85
    final_price = president_apartment * day_for_rest
elif day_for_rest > 15 and accommodation == 'president apartment':
    president_apartment = president_apartment * 0.80
    final_price = president_apartment * day_for_rest

if grade == 'positive':
    grade_price = final_price * 0.25
    final_price = grade_price + final_price
elif grade == 'negative':
    final_price = final_price * 0.90

print(f'{final_price:.2f}')
