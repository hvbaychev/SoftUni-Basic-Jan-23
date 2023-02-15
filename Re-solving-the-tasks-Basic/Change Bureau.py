number_bitcoin = int(input())
number_joan = float(input())
commission = float(input())

bitcoin_price = 1168 * number_bitcoin
joan_price_usd = 0.15 * number_joan
dollar_price = 1.76 * joan_price_usd
euro_price = 1.95

total_sum = bitcoin_price + dollar_price
in_euro = total_sum / euro_price

comm = (commission / 100) * in_euro
final = in_euro - comm

print(f'{final:.2f}')