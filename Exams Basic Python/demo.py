card_player_one_int = int(input())
card_player_two_int = int(input())
if card_player_one_int > card_player_two_int:
    player_one_sum += card_player_one_int - card_player_two_int
elif card_player_one_int < card_player_two_int:
    player_two_sum = card_player_two_int - card_player_one_int
    break