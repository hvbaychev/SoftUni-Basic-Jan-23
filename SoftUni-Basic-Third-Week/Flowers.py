chrysanthemums_bought = int(input())
rose_bought = int(input())
tulip_bought = int(input())
season = input()
celebration_day = input()

chrysanthemums = 0.00
rose = 0.00
tulip = 0.00
total_bouquet = 0.00
total_sum = 0.00
arrangement = 2.00

total_bouquet = chrysanthemums_bought + rose_bought + tulip_bought

if (season == 'Spring' or season == 'Summer') and celebration_day == 'N':
    chrysanthemums = 2.00 * chrysanthemums_bought
    rose = 4.10 * rose_bought
    tulip = 2.50 * tulip_bought
elif (season == 'Autumn' or season == 'Winter') and celebration_day == 'N':
    chrysanthemums = 3.75 * chrysanthemums_bought
    rose = 4.50 * rose_bought
    tulip = 4.15 * tulip_bought

if (season == 'Spring' or season == 'Summer') and celebration_day == 'Y':
    chrysanthemums = (2.00 * chrysanthemums_bought) * 1.15
    rose = (4.10 * rose_bought) * 1.15
    tulip = (2.50 * tulip_bought) * 1.15
elif (season == 'Autumn' or season == 'Winter') and celebration_day == 'Y':
    chrysanthemums = (3.75 * chrysanthemums_bought) * 1.15
    rose = (4.50 * rose_bought) * 1.15
    tulip = (4.15 * tulip_bought) * 1.15

total_sum = chrysanthemums + rose + tulip

if tulip_bought >= 7 and season == 'Spring':
    total_sum = total_sum * 0.95
elif rose_bought >= 10 and season == 'Winter':
    total_sum = total_sum * 0.90

if total_bouquet >= 20 and (season == 'Spring' or season == 'Summer' or season == 'Winter' or season == 'Autumn'):
    total_sum = total_sum * 0.80

total_sum = total_sum + arrangement

print(f'{total_sum:.2f}')
