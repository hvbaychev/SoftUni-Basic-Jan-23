number = int(input())

bonus = 0

if number <= 100:
    bonus += 5
elif number <= 1000:
    bonus = number * 0.20
else:
    bonus = number * 0.10

if number % 2 == 0:
    bonus += 1
if number % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + number)

