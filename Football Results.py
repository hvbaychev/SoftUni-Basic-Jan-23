result_first_game = input()
result_second_game = input()
result_third_game = input()

win = 0
draw = 0
lose = 0

first_char_game_one = result_first_game[0]
second_char_game_two = result_first_game[2]

if first_char_game_one > second_char_game_two:
    win = win + 1
elif first_char_game_one == second_char_game_two:
    draw = draw + 1
elif first_char_game_one < second_char_game_two:
    lose = lose + 1

first_char_second_game = result_second_game[0]
second_char_second_game = result_second_game[2]

if first_char_second_game > second_char_second_game:
    win = win + 1
elif first_char_second_game == second_char_second_game:
    draw = draw +1
elif first_char_second_game < second_char_second_game:
    lose = lose + 1

first_char_third_game = result_third_game[0]
second_char_third_game = result_third_game[2]

if first_char_third_game > second_char_third_game:
    win = win + 1
elif first_char_third_game == second_char_third_game:
    draw = draw + 1
elif first_char_third_game < second_char_third_game:
    lose = lose + 1

print(f'Team won {win} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {draw}')



