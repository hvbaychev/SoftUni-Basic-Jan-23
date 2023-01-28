number_eggs_player_one = int(input())
number_eggs_player_two = int(input())


while number_eggs_player_one > 0 and number_eggs_player_two > 0:
    command = input()
    if command == 'End':
        print(f"Player one has {number_eggs_player_one} eggs left.")
        print(f"Player two has {number_eggs_player_two} eggs left.")
        break
    elif command == 'one':
        number_eggs_player_two -= 1
    elif command == 'two':
        number_eggs_player_one -= 1

if number_eggs_player_one > number_eggs_player_two and command != 'End':
    print(f"Player two is out of eggs. Player one has {number_eggs_player_one} eggs left.")
elif number_eggs_player_two > number_eggs_player_one and command != 'End':
    print(f"Player one is out of eggs. Player two has {number_eggs_player_two} eggs left.")
