count_eggs_first_player = int(input())
count_eggs_second_player = int(input())

while True:
    command = input()
    winner = command
    if winner == "one":
        count_eggs_second_player = count_eggs_second_player - 1
    elif winner == "two":
        count_eggs_first_player = count_eggs_first_player - 1

    if count_eggs_first_player <= 0:
        print(f"Player one is out of eggs. Player two has {count_eggs_second_player} eggs left.")
        break
    elif count_eggs_second_player <= 0:
        print(f"Player two is out of eggs. Player one has {count_eggs_first_player} eggs left.")
        break
    elif command == "End":
        print(f"Player one has {count_eggs_first_player} eggs left.")
        print(f"Player two has {count_eggs_second_player} eggs left.")
        break