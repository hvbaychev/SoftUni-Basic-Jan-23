import sys

bread = int(input())
points = 0
best_point = -sys.maxsize
best_backer = ''

for food in range(bread):

    name = input()
    while True:
        evaluation = input()

        if evaluation == 'Stop':
            break

        evaluation = int(evaluation)

        points += evaluation

    print(f"{name} has {points} points.")
    if points > best_point:
        best_backer = name
        best_point = points
        print(f"{best_backer} is the new number 1!")
    points = 0

print(f"{best_backer} won competition with {best_point} points!")