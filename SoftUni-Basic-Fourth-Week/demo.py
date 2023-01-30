capacity = int(input())
counter = 0
money_income = 0
money = 0
people = 0
command = input()
cinemaFull = 'false'

while command != "Movie time!":
    number_people = int(command)
    # Ако в залата се опитат да влязат повече хора от колкото места са останали,
    # то се счита че местата са изчерпани и програмата трябва да приключи четенето на вход
    if number_people + people > capacity:
        cinemaFull = 'true'
        break

    people += number_people

    money_income = number_people * 5

    if number_people % 3 == 0:
        money_income -= 5

    money += money_income

    command = input()

if cinemaFull == 'true':
    print(f"The cinema is full.\nCinema income - {money:.0f} lv.")
else:
    print(f"There are {capacity - people} seats left in the cinema.\nCinema income - {money:.0f} lv.")