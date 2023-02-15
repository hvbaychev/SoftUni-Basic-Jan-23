groups = int(input())
total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for gr in range(groups):
    people = int(input())
    total_people += people
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilimandjaro += people
    elif 26 <= people <= 40:
        k2 += people
    else:
        everest += people

p1 = (musala / total_people) * 100
p2 = (monblan / total_people) * 100
p3 = (kilimandjaro / total_people) * 100
p4 = (k2 / total_people) * 100
p5 = (everest / total_people) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')


