fruit = input()
pack = input()
pack_num = int(input())

price = 0
discount = 0
final_price = 0

if fruit == "Watermelon":
    if pack == "small":
        price = 56.00 * 2
    elif pack == "big":
        price = 28.70 * 5
elif fruit == "Mango":
    if pack == "small":
        price = 36.66 * 2
    elif pack == "big":
        price = 19.60 * 5
elif fruit == "Pineapple":
    if pack == "small":
        price = 42.10 * 2
    elif pack == "big":
        price = 24.80 * 5
else:
    if pack == "small":
        price = 20.00 * 2
    elif pack == "big":
        price = 15.20 * 5

price_to_pay = price * pack_num

if 400 <= price_to_pay <= 1000:
    discount = price_to_pay * 0.15
    final_price = price_to_pay - discount
elif price_to_pay > 1000:
    discount = price_to_pay * 0.50
    final_price = price_to_pay - discount
else:
    final_price = price_to_pay

print(f"{final_price:.2f} lv.")