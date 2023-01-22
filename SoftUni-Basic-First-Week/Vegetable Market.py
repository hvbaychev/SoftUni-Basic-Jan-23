euro = 1.94

priceKgZel = float(input())
priceKgPlod = float(input())
sumKgZel = float(input())
sumKgPlod = float(input())

totalZelPrice = priceKgZel * sumKgZel
totalPldPrice = priceKgPlod * sumKgPlod

totalSumEuro = (totalPldPrice + totalZelPrice) / euro

print('%.2f' % float(totalSumEuro))