import math

tournament = int(input())
entry_points = float(input())

w = 2000
f = 1200
sf = 720

count_win = 0
winning_points = 0

for i in range(tournament):
    if i <= tournament:
        stage = input()
        if stage == 'W':
            winning_points += w
            count_win += 1
        elif stage == 'F':
            winning_points += f
        elif stage == 'SF':
            winning_points += sf

total_points = entry_points + winning_points
average_points = winning_points / tournament

percent_win_tournament = (count_win / tournament) * 100

print(f'Final points: {total_points:.0f}')
print(f'Average points: {math.floor(average_points):.0f}')
print(f'{percent_win_tournament:.2f}%')
