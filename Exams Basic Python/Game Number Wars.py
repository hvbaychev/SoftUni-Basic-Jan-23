first_player = input()
second_player = input()

player_one_sum = 0
player_two_sum = 0


points = 0
winner = 0

equal = 'true'
win_one = 'true'
win_two = 'true'

card_player_one_int = 0
card_player_two_int = 0

while True:
    card_player_one = input()
    if card_player_one == 'End of game':
        win_one = 'false'
        break

    card_player_two = input()
    if card_player_two == 'End of game':
        win_two = 'false'
        break

    card_player_one_int = int(card_player_one)
    card_player_two_int = int(card_player_two)

    if card_player_one_int > card_player_two_int:
        player_one_sum += card_player_one_int - card_player_two_int
    elif card_player_one_int < card_player_two_int:
        player_two_sum += card_player_two_int - card_player_one_int
    elif card_player_one_int == card_player_two_int:
        card_player_one_int = int(input())
        card_player_two_int = int(input())
        if card_player_one_int > card_player_two_int:
            equal = 'false'
            break
        elif card_player_one_int < card_player_two_int:
            equal = 'false'
            break


if win_one == 'false' or win_two == 'false':
    print(f'{first_player} has {player_one_sum} points')
    print(f'{second_player} has {player_two_sum} points')
if equal == 'false':
    print("Number wars!")
    if card_player_one_int > card_player_two_int:
        print(f"{first_player} is winner with {player_one_sum} points")
    else:
        print(f"{second_player} is winner with {player_two_sum} points")