line = input().lower()
sum_vowels = 0

for x in line:
    if x == 'a':
        sum_vowels += 1
    elif x == 'e':
        sum_vowels += 2
    elif x == 'i':
        sum_vowels += 3
    elif x == 'o':
        sum_vowels += 4
    elif x == 'u':
        sum_vowels += 5

print(sum_vowels)

