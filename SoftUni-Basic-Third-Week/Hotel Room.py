month = input()
nights = int(input())

price_flat = 0.00
price_studio = 0.00
studio = 0.00
flat = 0.00

if month == 'May' or month == 'October':
    studio = 50
    flat = 65
elif month == 'June' or month == "September":
    studio = 75.20
    flat = 68.70
elif month == 'July' or month == 'August':
    studio = 76
    flat = 77

if month == 'May' or month == 'October':
    if 7 < nights < 14:
        price_studio = (studio * nights) * 0.95
    elif nights > 14:
        price_studio = (studio * nights) * 0.70
    else:
        price_studio = studio * nights

if month == 'May' or month == 'October':
    if 7 < nights <= 14:
        price_flat = flat * nights
    elif nights > 14:
        price_flat = (flat * nights) * 0.90
    else:
        price_flat = flat * nights

if month == 'June' or month == 'September':
    if nights > 14:
        price_studio = (studio * nights) * 0.80
    else:
        price_studio = studio * nights

if month == 'June' or month == 'September':
    if nights > 14:
        price_flat = (flat * nights) * 0.90
    else:
        price_flat = flat * nights

if month == 'July' or month == 'August':
    price_studio = studio * nights

if month == 'July' or month == 'August':
    if nights > 14:
        price_flat = (flat * nights) * 0.90
    else:
        price_flat = flat * nights


print(f'Apartment: {price_flat:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')





