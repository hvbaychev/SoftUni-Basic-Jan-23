priceNylon = 1.50
pricePaint = 14.50
priceThinner = 5.00
pricePack = 0.40

needNylon = int(input())
needPaint = int(input())
needThinner = int(input())
hoursForWorkers = int(input())

totalNylon = needNylon + 2
totalPaint = needPaint * 0.10


sumForNylon = totalNylon * priceNylon
sumForPaint = (needPaint + totalPaint) * pricePaint
sumForThinner = needThinner * priceThinner

totalSumForMaterials = sumForNylon + sumForPaint + sumForThinner + pricePack

sumForWorkers = (totalSumForMaterials * 0.30) * hoursForWorkers

finalPrice = totalSumForMaterials + sumForWorkers

print(finalPrice)