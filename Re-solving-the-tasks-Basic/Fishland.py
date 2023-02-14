skumria_kg = float(input())
caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumria_kg * 1.6 * palamud_kg
safrid_price = caca_kg * 1.8 * safrid_kg
midi_price = midi_kg * 7.50
total = palamud_price + safrid_price + midi_price
print(f'{total:.2f}')
