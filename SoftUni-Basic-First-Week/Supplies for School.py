priceOfPen = 5.80
priceOfMark = 7.20
chemicalPerLiter = 1.20

packOfPen = int(input())
packOfMark = int(input())
litreChemical = int(input())
percentDiscount = int(input()) / 100


totalPriceForPen = priceOfPen * packOfPen
totalPriceForMark = priceOfMark * packOfMark
totalPriceForChemical = chemicalPerLiter * litreChemical

totalPriceForAll = totalPriceForPen + totalPriceForMark + totalPriceForChemical

priceAfterDiscount = totalPriceForAll - (totalPriceForAll * percentDiscount)

print(priceAfterDiscount)