import math

count_tournament = int(input())
starting_points = int(input())

points_sum = 0
average = 0
percent_win = 0
win = 0
final_points = 0

for _ in range(count_tournament):
    stage_tournament = input()
    if stage_tournament == 'W':
        w = 2000
        points_sum += w
        win += 1
    elif stage_tournament == 'F':
        f = 1200
        points_sum += f
    elif stage_tournament == 'SF':
        sf = 720
        points_sum += sf

final_points = points_sum + starting_points
average = points_sum / count_tournament
percent_win = (win / count_tournament) * 100

print(f"Final points: {final_points:.0f}")
print(f"Average points: {math.floor(average):.0f}")
print(f"{percent_win:.2f}%")


