club_name = input()
game_number = int(input())

w = 3
w_count = 0
w_percent = 0
d = 1
d_count = 0
l = 0
l_count = 0

total_points = 0

for _ in range(game_number):
    result = input()
    if result == 'W':
        w_count += 1
        total_points += w
    elif result == 'D':
        d_count += 1
        total_points += d
    elif result == 'L':
        l_count += 1
        total_points += l

if game_number == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    w_percent = (w_count / game_number) * 100
    print(f"{club_name} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w_count}")
    print(f"## D: {d_count}")
    print(f"## L: {l_count}")
    print(f"Win rate: {w_percent:.2f}%")
