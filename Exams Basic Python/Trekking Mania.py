climbers = int(input())

musala = 0
moblant = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(climbers):
    number_people = int(input())
    total_people += number_people
    if number_people <= 5:
        musala += number_people
    elif 6 <= number_people <= 12:
        moblant += number_people
    elif 13 <= number_people <= 25:
        kilimandjaro += number_people
    elif 26 <= number_people <= 40:
        k2 += number_people
    else:
        everest += number_people

musala = (musala / total_people) * 100
moblant = (moblant / total_people) * 100
kilimandjaro = (kilimandjaro / total_people) * 100
k2 = (k2 / total_people) * 100
everest = (everest / total_people) * 100

print(f'{musala:.2f}%')
print(f'{moblant:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')
