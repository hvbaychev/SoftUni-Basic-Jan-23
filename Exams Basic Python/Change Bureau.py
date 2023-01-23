bitcoin_amount = int(input())
yuan = float(input())
commission = float(input())

bitcoin = 1168 * bitcoin_amount
dollar = 1.76
chin_yuan = 0.15 * yuan * dollar
euro = 1.95

total_sum = bitcoin + chin_yuan

total_sum = total_sum / euro

comiss = commission * (1 / 100)
comiss = comiss * total_sum

total_sum = total_sum - comiss

print(f'{total_sum:.2f}')