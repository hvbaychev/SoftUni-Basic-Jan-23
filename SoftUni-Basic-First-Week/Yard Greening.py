yard_area = float(input())
price = 7.61 * yard_area

final_price = price * (100 - 18) / 100

discount = price - final_price

print(f"The final price is: {final_price} lv")
print(f"The final discount is: {discount} lv")