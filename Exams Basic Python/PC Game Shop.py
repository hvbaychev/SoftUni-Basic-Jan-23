sale_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for _ in range(sale_games):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {(hearthstone/sale_games) * 100:.2f}%")
print(f"Fornite - {(fornite/sale_games) * 100:.2f}%")
print(f"Overwatch - {(overwatch/sale_games) * 100:.2f}%")
print(f"Others - {(others/sale_games) * 100:.2f}%")