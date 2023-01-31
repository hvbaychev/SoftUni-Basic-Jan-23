line = input().lower()
sum_vowels = 0

for cycle in line:
    if cycle == 'a':
        sum_vowels += 1
    elif cycle == 'e':
        sum_vowels += 2
    elif cycle == 'i':
        sum_vowels += 3
    elif cycle == 'o':
        sum_vowels += 4
    elif cycle == 'u':
        sum_vowels += 5

print(sum_vowels)
