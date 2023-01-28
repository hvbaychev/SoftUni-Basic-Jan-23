number_client = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for _ in range(number_client):
    exercise = input()
    if exercise == 'Back':
        back += 1
    elif exercise == 'Chest':
        chest += 1
    elif exercise == 'Legs':
        legs += 1
    elif exercise == 'Abs':
        abs += 1
    elif exercise == 'Protein shake':
        protein_shake += 1
    elif exercise == 'Protein bar':
        protein_bar += 1

total_train = back + chest + legs + abs
total_buy = protein_shake + protein_bar

total_train_percent = (total_train / number_client) * 100
total_buy_percent = (total_buy / number_client) * 100


print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{total_train_percent:.2f}% - work out")
print(f"{total_buy_percent:.2f}% - protein")
