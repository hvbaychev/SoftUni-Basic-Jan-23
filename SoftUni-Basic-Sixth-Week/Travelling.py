destination = input()
saved_money = 0
while destination != 'End':
    need_money = float(input())
    while saved_money <= need_money:
        money = float(input())
        saved_money += money
        if saved_money >= need_money:
            print(f"Going to {destination}!")
            break
    saved_money = 0
    destination = input()
