price_t_shirt = float(input())
win_sum = float(input())

discount = 15/100

short_price = price_t_shirt * 0.75
socks_price = short_price * 0.20
shoes = (short_price + price_t_shirt) * 2
total_equipment = short_price + socks_price + shoes + price_t_shirt

final_price_after_discount = total_equipment * discount
final = total_equipment - final_price_after_discount

if final >= win_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final:.2f} lv.")
else:
    diff = abs(final - win_sum)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")