name_tournament = input()
game_counter = 0
total_game_counter = 0
win_counter = 0
lose_counter = 0

while name_tournament != 'End of tournaments':
    game_tournament = int(input())
    for game in range(game_tournament):
        our_team = int(input())
        enemy_team = int(input())
        game_counter += 1
        total_game_counter += 1
        diff = abs(our_team - enemy_team)
        if our_team > enemy_team:
            win_counter += 1
            print(f'Game {game_counter} of tournament {name_tournament}: win with {diff:.0f} points.')
        else:
            lose_counter += 1
            print(f'Game {game_counter} of tournament {name_tournament}: lost with {diff:.0f} points.')

    name_tournament = input()
    game_counter = 0

print(f'{(win_counter / total_game_counter) * 100:.2f}% matches win')
print(f'{(lose_counter / total_game_counter) * 100:.2f}% matches lost')
