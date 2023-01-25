climbers = int(input())

sum_of_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0


for i in range(climbers):
    number_of_people = int(input())
    sum_of_people += number_of_people
    if number_of_people <= 5:
        musala += number_of_people
    elif 6 <= number_of_people <= 12:
        monblan += number_of_people
    elif 13 <= number_of_people <= 25:
        kilimandjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        k2 += number_of_people
    else:
        everest += number_of_people

musala = (musala / sum_of_people) * 100
monblan = (monblan / sum_of_people) * 100
kilimandjaro = (kilimandjaro / sum_of_people) * 100
k2 = (k2 / sum_of_people) * 100
everest = (everest / sum_of_people) * 100

print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')

