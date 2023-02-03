import math

money = float(input())
change_money = money * 100
coin = 0

while change_money > 0:
    change_money = math.floor(change_money)
    if change_money >= 200:
        change_money -= 200
        coin += 1
    elif 200 > change_money >= 100:
        change_money -= 100
        coin += 1
    elif 100 > change_money >= 50:
        change_money -= 50
        coin += 1
    elif 50 > change_money >= 20:
        change_money -= 20
        coin += 1
    elif 20 > change_money >= 10:
        change_money -= 10
        coin += 1
    elif 10 > change_money >= 5:
        change_money -= 5
        coin += 1
    elif 5 > change_money >= 2:
        change_money -= 2
        coin += 1
    elif 2 > change_money >= 1:
        change_money -= 1
        coin += 1

print(coin)

