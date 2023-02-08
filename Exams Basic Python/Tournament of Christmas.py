day_tournament = int(input())

count_win = 0
count_lose = 0
daily_win = 0
daily_lose = 0
spent_money = 20
win_money = 0
total_sum = 0

for day in range(1, day_tournament + 1):
    if daily_win > daily_lose:
        win_money *= 1.10
        total_sum += win_money
        win_money = 0
        daily_win = 0
        daily_lose = 0
    else:
        total_sum += win_money
        win_money = 0
        daily_win = 0
        daily_lose = 0

    while True:
        sport = input()

        if sport == 'Finish':
            break

        result = input()

        if result == 'win':
            win_money += spent_money
            count_win += 1
            daily_win += 1
        elif result == 'lose':
            count_lose += 1
            daily_lose += 1

if daily_win > daily_lose:
    win_money *= 1.10
    total_sum += win_money
    win_money = 0
    daily_win = 0
    daily_lose = 0

if count_win > count_lose:
    total_sum = total_sum * 1.20
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")
