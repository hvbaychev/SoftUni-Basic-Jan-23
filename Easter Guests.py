import math

guest = int(input())
money = int(input())

bread = 4
egg = 0.45

number_bread = math.ceil(guest / 3)
number_eggs = guest * 2

bread_price = number_bread * bread
eggs_price = number_eggs * egg

total_price = bread_price + eggs_price
remain_money = abs(money - total_price)

if money >= total_price:
    print(f"Lyubo bought {number_bread} Easter bread and {number_eggs} eggs.")
    print(f"He has {remain_money:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {remain_money:.2f} lv. more.")