temperature = float(input())
part_of_the_day = input()

outfit = ''
shoes = ''

if 10 <= temperature <= 18:
    if part_of_the_day == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")

if 18 < temperature <= 24:
    if part_of_the_day == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")

if temperature >= 25:
    if part_of_the_day == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")
    elif part_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {temperature:.0f} degrees, get your {outfit} and {shoes}.")