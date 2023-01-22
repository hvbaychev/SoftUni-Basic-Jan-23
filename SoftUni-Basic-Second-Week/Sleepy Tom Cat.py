import math

rest_days = int(input())
year_days = 365
after_work = 63
resting_days = 127
tom_play_per_year = 30000


game_in_rest_days = rest_days * resting_days
game_working_days = (year_days - rest_days) * after_work

total_time_play = game_working_days + game_in_rest_days

need_more_to_play = abs(tom_play_per_year - total_time_play)

hours = abs(need_more_to_play) // 60
minutes = abs(need_more_to_play) % 60

if total_time_play > tom_play_per_year:
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f"{hours} hours and {minutes} minutes less for play")



